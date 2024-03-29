from Bio import Entrez

def parse_author(author_info):
    '''
    Takes a pubmed entry's author info and returns lastname, forename.
    '''
    last = author_info['LastName']
    forename = author_info['ForeName']
    name = ", ".join([last, forename])
    return name


def parse_journal(journal_info, pagination):
    '''
    Takes a pubmed entry's journal publication info and returns issue information.
    '''
    abbrev = journal_info['ISOAbbreviation']

    if 'JournalIssue' in journal_info:
        issue = journal_info['JournalIssue']
        if pagination and ('Issue' in issue):
            issue = ', '.join([abbrev, issue['Volume'], issue['Issue'], pagination['MedlinePgn']])
        elif 'Volume' in issue:
            issue = ', '.join([abbrev, issue['Volume']])
        else:
            issue = abbrev
    else:
        issue = abbrev
    return issue


class Paper(object):
    def __init__(self, pubmed_entry):
        article_info = pubmed_entry['MedlineCitation']['Article']
        #author info
        authors = article_info['AuthorList']
        if len(authors) < 3:
            self.first_author = (', '.join([parse_author(author) for author in authors]) + '.')
        else:
            self.first_author = (parse_author(authors[0]) + ' et al.')
        #article info
        if len(article_info['ArticleDate']):
            self.year = article_info['ArticleDate'][0]['Year']
        elif ('PubDate' in article_info['Journal']['JournalIssue']) and ('Year' in article_info['Journal']['JournalIssue']['PubDate']):
            self.year = article_info['Journal']['JournalIssue']['PubDate']['Year']
        else:
            self.year = ''
        self.title = article_info['ArticleTitle'].strip("'")
        pagination = False
        if "Pagination" in article_info :
            pagination = article_info['Pagination']
        self.journal_info = parse_journal(article_info['Journal'], pagination)
        if len(article_info["ELocationID"]):
            self.link = str('https://doi.org/' + article_info['ELocationID'][-1])
        else:
            self.link = ''
        self.yml = '''- author: {}\n  title: "{} {}."\n  alt_link: "{}"\n  year: {}\n\n'''.format(self.first_author, self.title, self.journal_info, self.link, self.year)


def search_author(query, email, max_search=60):
    Entrez.email = email
    handle = Entrez.esearch(db='pubmed',
                            retmax=max_search,
                            retmode='XML',
                            term=query)
    results = Entrez.read(handle)
    return results['IdList']



def fetch_details(id_list, email):
    ids = ','.join(id_list)
    Entrez.email = email
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results['PubmedArticle']

def fetch_new_papers(ids, email):
    '''
    Fetch only new papers, and update the recent_pubmed_ids.txt list.
    If no new papers found, stop.
    '''
    a = open('_data/recent_pubmed_ids.txt', 'r')
    previous_ids = a.read().split(',')
    a.close()
    ids = [i for i in ids if i not in previous_ids]

    if len(ids) > 0:
        #only fetch if there are new ids
        results = fetch_details(ids, email)
        papers = [Paper(i).yml for i in results]


        #update recent_pubmed_ids
        a = open('_data/recent_pubmed_ids.txt', 'w')
        a.write(','.join(ids + previous_ids))
        a.close()

        return papers
    else:
        print("No new papers found.")


def add_new_papers(new_papers):
    if new_papers:
        append_copy = open("_data/papers.yml", "r")
        original_text = append_copy.read()
        append_copy.close()

        new_papers = ''.join(new_papers)

        append_copy = open("_data/papers.yml", "w")
        append_copy.write(new_papers)
        append_copy.write(original_text)
        append_copy.close()


def main():
    # change these for your own website
    user_email = 'lina.mntran@gmail.com'
    author = 'Frankland PW[Author] or Josselyn SA[Author]'

    # search the author, find paper details and add to papers.yml
    append_copy = open("_data/papers.yml", "r")
    current_papers = append_copy.read()
    append_copy.close()
    if len(current_papers) == 0:
        ids = search_author(author, user_email, 200)
    else:
        ids = search_author(author, user_email, 200)
    papers = fetch_new_papers(ids, user_email)
    if papers is not None:
        add_new_papers(papers)
        print("Added {} new papers.".format(len(papers)))


if __name__ == '__main__':
    main()
