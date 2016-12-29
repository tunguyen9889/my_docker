
curl -siX POST -H "Content-Type: application/json" -d "{
  \"team_name\": \"${CI_PROJECT_DIR:8}\",
  \"competition_round\": \"${ROUND}\"
}" "http://scorer.honestbee.com:5000/submit"
