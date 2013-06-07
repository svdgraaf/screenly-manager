DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/$DISPLAY xwd -root > /tmp/screenshot.xwd
convert /tmp/screenshot.xwd /home/pi/screenly/static/img/screenshot.png