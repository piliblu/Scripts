#!/bin/bash
_user="$(id -u -n)"
_uid="$(id -u)"
echo "User name : $_user"
echo "User name ID (UID) : $_uid"
If [ $_user < 1000]
Echo “Welcome System user!”
