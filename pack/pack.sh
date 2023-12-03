

rm -rf release
pip install -r req.txt --prefix release --ignore-installed
wget https://raw.githubusercontent.com/Bhagyarsh/usim800/master/usim800/Sms/sms.py -O ./release/lib/python3.11/site-packages/usim800/Sms/sms.py
cp ../apiserver.py release/

pkg_path=`cd release && find . -type d -name site-packages`
echo "#/bin/bash
PYTHONPATH=$pkg_path python apiserver.py \"$@\"
" > release/entry.sh
chmod +x release/entry.sh

