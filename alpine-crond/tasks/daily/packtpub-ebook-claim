#!/bin/sh

# Check user agent https://myusers.info/client/safari
# Script author https://github.com/igustin/packt

USERID="${PACKTEMAIL}"   # Packt userid
PASSWORD="${PACKTPASSWD}"       # Packt password
DLDIR="/tmp"
COOKIE="${DLDIR}/cookie.txt"    # cookie file

# web login
curl -k -fsSL -b ${COOKIE} -c ${COOKIE} -d "email=${USERID}" -d "password=${PASSWORD}" -d "op=Login" -d "form_build_id=form-af740361add1f4e5a38706755a15583a" -d "form_token=131453af75e4d0dbb10b5993d25dae86" -d "form_id=packt_user_login_form" https://www.packtpub.com >/dev/null 2>&1

# daily free e-book
curl -k -s https://www.packtpub.com/packt/offers/free-learning > ${DLDIR}/packt_daily.html

TITLE=$(grep "dotd-title" -A 2 ${DLDIR}/packt_daily.html | tail -1 | sed 's/^[^0-9A-Za-z]*//;s/[\t ]*<\/h2>$//' | awk '{$2=$2};1' | sed 's/ /_/g')

# claim
CLAIM=$(grep -oE "freelearning-claim/[0-9]+/[0-9]+" ${DLDIR}/packt_daily.html)
curl -k -fsSL -b ${COOKIE} -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.5' -H 'Connection: keep-alive' -H 'Host: www.packtpub.com' -H 'Referer: https://www.packtpub.com/packt/offers/free-learning' "https://www.packtpub.com/${CLAIM}" >/dev/null 2>&1

# download link
BOOK=$(echo ${CLAIM} | sed 's/.*\/\([0-9]*\)\/.*/\1/')

# Send message to Slack
WEBHOOKURL="${SLACKHOOK}"
: "${MESSAGE:=eBook of the day: *$TITLE*.\nDownload link <https://www.packtpub.com/ebook_download/$BOOK/pdf | here>!}"
curl -k -fsSL -X POST --data-urlencode 'payload={"username": "PacktpubBot", "text": "'"$MESSAGE"'", "icon_emoji": ":ghost:"}' ${WEBHOOKURL}

# Packt logout
curl -k -fsSL -b "${COOKIE}" -c "${COOKIE}" https://www.packtpub.com/logout > packt_logout.html

rm -rfv ${COOKIE} ${DLDIR}/packt_daily.html

# end
