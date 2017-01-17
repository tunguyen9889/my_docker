#!/usr/bin/env sh

CONFIG_FILE=/usr/app/.hz/schema.toml

HORIZON_SCHEMA=${HORIZON_SCHEMA:-""}

HORIZON_SCHEMA+=$(cat << EOF

[groups.supervisor]
[groups.supervisor.rules.carte_blanche]
template = "any()"
[groups.agent]
[groups.agent.rules.read_cars]
template = "collection('cars').anyRead()"
[groups.agent.rules.read_orders]
template = "collection('orders').anyRead()"
[groups.agent.rules.any_bookmarks]
template = "collection('bookmarks').any()"
[groups.agent.rules.any_order_editing]
template = "collection('order_editing').any()"
[groups.agent.rules.read_statistics]
template = "collection('statistics').anyRead()"
[groups.agent.rules.read_messages]
template = "collection('messages').anyRead()"
[groups.admin]
[groups.admin.rules.carte_blanche]
template = "any()"

EOF
)

cat << EOF > ${CONFIG_FILE}

${HORIZON_SCHEMA}

EOF
