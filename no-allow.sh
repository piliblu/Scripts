#!/bin/bash
_user="$(id -u -n)"
_uid="$(id -u)"
echo "User name : $_user"
echo "User name ID (UID) : $_uid"
if [ $_uid -lt 1000 ]
then
echo "Welcome System user!"
else
echo "This is a protected system, if you're not authorized disconnect this session immediately."
fi
