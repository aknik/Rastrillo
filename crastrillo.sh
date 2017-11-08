RET=1 
until [ ${RET} -eq 0 ]; 
do ncftpput -DD -z -u 
user -p password remoteserver /remote/dir /local/file 
RET=$? 
sleep 10 
done

