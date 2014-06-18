# based on https://forums.robertsspaceindustries.com/discussion/comment/2801458/#Comment_2801458

if starting: #settings
	vJoyId = 0		
	usePadels = False	
	pedalsJoyId = 1
	#maximum angle reached by your freeTrack (game value)
	maxanglex = 100
	maxangley = 90
	# Change this if you want quicker mouse movement:
	mousemultiply = 20
	#how much do you lean to trigger the button (freeTrack.z value)
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
# angle = freeTrack.axis value
# maxa = freeTrack axis maximum angle
# intv = intvalue
# mult = non linear multiplicator
# nlstart = until which freeTrack.axis angle do the nonlinear part works
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

	vJoy[vJoyId].rx = int(round(nonlinear(freeTrack.yaw, maxanglex, intvalue, nlmult, nlstart)*leanspeed))
	vJoy[vJoyId].ry = int(round(nonlinear(freeTrack.pitch, maxangley, intvalue, nlmult, nlstart)*leanspeed))

	if freeTrack.z > lean and freeTrack.z < (lean + 5) :
		vJoy[vJoyId].setButton(0,True)
		leanspeed = leanslower
	else :	
		vJoy[vJoyId].setButton(0,False)

	if freeTrack.z > lean2 and freeTrack.z < (lean2 + 5) :
		vJoy[vJoyId].setButton(1, True)
	else : 
		vJoy[vJoyId].setButton(1, False)
		leanspeed = 1

if starting:
	global leanspeed
	leanspeed = 1.0
	running = True
	freeTrack.update += update

disable = keyboard.getPressed(Key.F11)

if disable:
	running = not running 
	vJoy[vJoyId].rx = 0
	vJoy[vJoyId].ry = 0
	#vJoy[vJoyId].z = 0

diagnostics.watch(vJoy[vJoyId].rx)
diagnostics.watch(vJoy[vJoyId].ry)
diagnostics.watch(freeTrack.yaw)
diagnostics.watch(freeTrack.pitch)
diagnostics.watch(freeTrack.z)
diagnostics.watch(vJoy[vJoyId].rz)