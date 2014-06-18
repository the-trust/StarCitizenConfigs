# based on https://forums.robertsspaceindustries.com/discussion/comment/2801458/#Comment_2801458

if starting: #settings
	vJoyId = 0		
	usePadels = False	
	pedalsJoyId = 1
	#maximum angle reached by your trackIR (game value)
	maxanglex = 100
	maxangley = 90
	# Change this if you want quicker mouse movement:
	mousemultiply = 20
	#how much do you lean to trigger the button (trackIR.z value)
	lean = -50
	lean2 = -10
	#reduce view speed while in zoomed in mode - keep this value <= 1 and > 0.
	leanslower = 0.5
	#nonlinear values
	nlmult = 3
	nlstart = 18
	#init
	intvalue = 16384
	modifier = 16.384

# pedals, uncomment to use
if usePadels:
	pedalsCombined = (0.5*joystick[pedalsJoyId].y - 0.5*joystick[pedalsJoyId].sliders[1])
	vJoy[vJoyId].rz = -1 * pedalsCombined * modifier

# The non linear function :
# angle = trackIR.axis value
# maxa = trackIR axis maximum angle
# intv = intvalue
# mult = non linear multiplicator
# nlstart = until which trackIR.axis angle do the nonlinear part works
def nonlinear(angle, maxa, intv, mult, nlstart):
	offset = int(round((intv*nlstart*mult)/maxa)) - int(round((intv*nlstart)/maxa))
	offset2 = int(round(offset/((intv-offset)/float(intvalue))))

	if angle < nlstart and angle > -nlstart :
		vjoyaxis = int(round((intv*angle*mult)/maxa))

	elif angle >= nlstart:
		vjoyaxis = int(round(((intv - offset2)*angle)/maxa)) + offset2

	elif angle <= -nlstart:
		vjoyaxis = int(round(((intv - offset2)*angle)/maxa)) - offset2
	return(vjoyaxis)

# the code
def update():
	global leanspeed
	if (not running):
		return

	vJoy[vJoyId].rx = int(round(nonlinear(trackIR.yaw, maxanglex, intvalue, nlmult, nlstart)*leanspeed))
	vJoy[vJoyId].ry = int(round(nonlinear(trackIR.pitch, maxangley, intvalue, nlmult, nlstart)*leanspeed))

	if trackIR.z > lean and trackIR.z < (lean + 5) :
		vJoy[vJoyId].setButton(0,True)
		leanspeed = leanslower
	else :	
		vJoy[vJoyId].setButton(0,False)

	if trackIR.z > lean2 and trackIR.z < (lean2 + 5) :
		vJoy[vJoyId].setButton(1, True)
	else : 
		vJoy[vJoyId].setButton(1, False)
		leanspeed = 1

if starting:
	global leanspeed
	leanspeed = 1.0
	running = True
	trackIR.update += update

disable = keyboard.getPressed(Key.F11)

if disable:
	running = not running 
	vJoy[vJoyId].rx = 0
	vJoy[vJoyId].ry = 0
	#vJoy[vJoyId].z = 0

diagnostics.watch(vJoy[vJoyId].rx)
diagnostics.watch(vJoy[vJoyId].ry)
diagnostics.watch(trackIR.yaw)
diagnostics.watch(trackIR.pitch)
diagnostics.watch(trackIR.z)
diagnostics.watch(vJoy[vJoyId].rz)