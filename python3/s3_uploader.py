#Requires .aws credentials at Home

#1st arg bucket name
#2nd project name or Folder
#3rd files path
import sys,os,glob,boto3

bkname=sys.argv[1]
prekee=sys.argv[2]+'/'
dir=sys.argv[3]
files=glob.glob(dir)
s3 = boto3.resource('s3')

for filename in files:
    kee = os.path.basename(filename)
    data = open(filename,'rb')
    s3.Bucket(bkname).put_object(Key=prekee+kee,Body=data)
    print("Uploaded "+filename+" to: "+prekee+kee)
    data.close()

