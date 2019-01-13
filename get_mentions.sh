FECHA=`date +%Y%m%d`
#nohup python3 python3/search3.py "@IvanDuque" ivanduque_2018&
if [ $# -eq 1 ]
then
	USERNAME=$1
	nohup python3 python3/search3.py "\"@${USERNAME}"\" ${USERNAME}_${FECHA}&
else
	echo "Only ONE parameter required. The account screen_name without the @"
fi

#exit(0)

