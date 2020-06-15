#!/bin/sh

# Decrypt the file
mkdir $HOME/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$CREDENTIALS_PASS" \
--output $HOME/secrets/credentials.json credentials.json.gpg
