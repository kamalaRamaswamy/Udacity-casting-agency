#!/bin/bash

export DATABASE_URL="postgresql://lukehaag:H2zw0XAuzYiKJ72K5SCBeOMQCkJFclMs@dpg-cfualr94reb6ks3msb2g-a.ohio-postgres.render.com/castingagency_tuh0"
export AUTH0_DOMAIN="dev-gtukrfvev3mrepk8.us.auth0.com"
export EXCITED="true"
export API_AUDIENCE="casting"
export ALGORITHMS='RS256'
export FLASK_APP=app

echo "setup.sh script executed successfully!"