docker run -it -v D:/HCMUT/PPL/2/BTL1/Ass1/MiniGO_BTL1:/usr/src/PPL ubuntu 
apt-get update
apt-get install -y python3 python3-pip
apt-get install -y default-jre default-jdk
export ANTLR_JAR="/usr/src/PPL/antlr-4.9.2-complete.jar"
python3 --version
java --version
echo $ANTLR_JAR
cd /usr/src/PPL
apt install python3.12-venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt