#!/usr/bin/env bash

python xmlrpc_client.py &
python xmlrpc_client.py &
python xmlrpc_client.py &
python xmlrpc_client.py &
python xmlrpc_client.py &

python xmlrpc_client2.py &
python xmlrpc_client2.py &
python xmlrpc_client2.py &
python xmlrpc_client2.py &
python xmlrpc_client2.py &

FAIL=0
sleep 2
for job in `jobs -p`; do
	wait $job || let "FAIL+=1"
done

if [ "$FAIL" == "0" ]; then
	echo "Done!"
else
	echo "FAIL! ($FAIL)"
fi
