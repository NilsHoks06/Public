#!/bin/bash

#Sets up a Raspberry PI Infotainment Screen automatically.
#Sorry english isn't my first language. I first made this script when i was new to scripting using bash, i thought it was fun this worked pretty well.
#I translated the script to english in comments.

#Updates packages
sudo apt-get update -y


#Installs X server og Openbox
sudo apt-get install -y xserver-xorg x11-xserver-utils xinit openbox
sudo apt-get install -y xserver-xorg-video-all


#Installs chromium browser
sudo apt-get install -y chromium

#Installs upgrades
sudo apt-get full-upgrade -y


#Removes old software
sudo apt-get autoremove -y
sudo apt-get autoclean -y


#Check if chromium already has ~/.config/chromium if not make one.
mkdir -p /home/pi/.config/chromium/Default
touch /home/pi/.config/chromium/'Local State'
touch /home/pi/.config/chromium/Default/Preferences
sudo chown -R pi:pi /home/pi/.config

#Autostart for Openbox
AUTOSTART="/etc/xdg/openbox/autostart"
#Marker to check if the script is already added. If it is it won't let you overwrite. Manual overwrite is "sudo nano /etc/openbox/autostart".
MARKER="# Start Chromium i kiosk modus"


#Create autostart if it doesn't exist.
if [ ! -f "$AUTOSTART" ]; then
    sudo tee "$AUTOSTART" > /dev/null << 'EOF'
#!/bin/sh
# Openbox autostart
EOF
    sudo chmod 755 "$AUTOSTART"
fi


#Add command to start chromium in kiosk mode at startup
if ! grep -q "$MARKER" "$AUTOSTART"; then
    sudo tee -a "$AUTOSTART" > /dev/null << 'EOF'

# Start Chromium i kiosk modus
xset s off
xset s noblank
xset -dpms

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/'Local State' || true
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences || true

#Here you can change your URL. Default is YouTube.
/usr/bin/chromium --disable-infobars --disable-features=TranslateUI --kiosk 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' &

EOF
fi

#Give access to autostart file
sudo chmod +x /etc/xdg/openbox/autostart

#Set up automatic start of X and Openbox at startup
cat > /home/pi/.xinitrc << 'EOF'
exec openbox-session
EOF

sudo chown pi:pi /home/pi/.xinitrc

if ! grep -q "startx" /home/pi/.bash_profile 2>/dev/null; then
    cat << 'EOF' >> /home/pi/.bash_profile

# Start X automatisk på tty1
if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
    startx -- -nocursor
fi
EOF
fi

#Give access to .bash_profile
sudo chown pi:pi /home/pi/.bash_profile

#Raspberry pi autologin at tty1
sudo raspi-config nonint do_boot_behaviour B2

read -p "Press ENTER to restart the configured infoscreen!"
sleep 2
sudo reboot