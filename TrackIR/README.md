Based on the superb work from sgtflyer on the RSI forums: https://forums.robertsspaceindustries.com/discussion/comment/2801458/#Comment_2801458
The his thread for more information!

Mini-Tutorial:

1) Download vjoy: https://sourceforge.net/projects/vjoystick/files/latest/download

2) Download FreePie: http://andersmalmgren.github.io/FreePIE/

3*) as of FreePie v1.5.459 you need the vjoy SDK: http://vjoystick.sourceforge.net/redirect_download_vJoy2SDK.php

4*) From the vjoy SDK, copy the SDK\lib\vJoyInterface.dll to your FreePie installation directory (and overwrite existing)

5) Configure vjoy device as you wish (you can enable all axis 4 PoVs and 32 button to be save)

6) Run TrackIR Software, optionally use the provided profile (TrackIR_profile.xml).

7) Start FreePie as administrator, and open the provided script FreePie_TrackIR.py, run with F5

8) Launch StarCitizen, run the command to load the provided action maps: pp_rebindkeys
"x:/path/to/StarCitizen_TrackIR_ActionMaps.xml"

9) Since vjoy probably runs ans js_1, it should work now.




