8/17/2015
=============
Driver version 2.5.0.0.  The executable has been digitally signed so that it is not flagged by Symantec's latest virus scan. 

This driver is for all of MaxLinear's USB UARTs.  This driver has been WHQL/HCK-certified on Windows 7.  The driver has been tested on Windows XP/7/8/8.1/10. The USB UARTs supported are:

	XR21V1410/1412/1414
	XR21B1411
	XR21B1420/1422/1424
	XR22801/802/804

This zip file contains the following folders:

	x64	= contains the 64-bit driver for 64-bit systems.
	x86	= contains the 32-bit driver for 32-bit systems.	
	EXE	= contains the executable that will uninstall previous driver installations, install the new driver, and search for any USB devices attached to the system. If installed using the EXE, the driver must be uninstalled using Programs and Features in the Control Panel.

Revision History (Rev. 2.2 to 2.5):
- (Rev 2.3 and 2.4 are un-released versions.)
- Added 15 Mbps baud rate support for XR2280x UARTs
- Added register read/write for XR2280x UARTs
- Added support for GPIOs 9-6 in driver and properties page for XR21B142x
- Added support for RS-485 mode using GPIO7/XEN for XR21B142x
- Added support for 1.5 stop bits for XR21B142x
- Changed default setting for dial-up support to "enabled" in properties page.
- Fixed modem input status bug
- Fixed memory leakage issues

Revision History (Rev. 2.1 to 2.2):
 - WHQL/HCK certified driver for Windows 8.1.  Driver will also work on Windows XP, Vista, 7 including Win XP Embedded, Win 7 Embedded and Windows Server.
 - Added support for XR21B1420/1422/1424 and XR22801/802/804.

Revision History (Rev. 2.0 to 2.1):
 - WHQL/HCK certified driver for Windows 8.1.  Driver will also work on Windows XP, Vista, 7 including Win XP Embedded, Win 7 Embedded and Windows Server.
 - Minor fixes to the logic to pass Windows 8.1 HCK testing.

Revision History (Rev. 1.9 to 2.0):
 - WHQL/HCK certified driver for Windows 8.  Driver will also work on Windows XP, Vista, 7 including Win XP Embedded, Win 7 Embedded and Windows Server.
 - Minor fixes to the logic to pass Windows 8 HCK testing.	

Revision History (Rev. 1.8 to 1.9):
 - Logic to override Writing to gpio-mode/dir/intmask, and char-format registers if the otp bit for the same is set in xr21b1411 device is implemented.
 - Failure to transfer using xmodem protocol is fixed.
 - Support for 9-bit mode for xr21v141x devices is enabled.
 - An ioctl is provided to get the VID, PID, and the channel number of the port opened.
 - Wide mode for xr21v141x device was being erroneously set while resuming from standby/hibernation is fixed.
 - Custom driver bit for xr21b1411 is now also set while resuming from standby/hibernation.
 - Gpio direction and int-mask registers are also restored while resuming from standby/hibernation.
 - Issues that were caused while asynchronous writes happen without waiting for the previous write to complete from the app is fixed.


Revision History (Rev. 1.7 to 1.8):
 - Fixed a blue-screen/crash issue when communication errors were generated .
 - Support for LowLatency/WideMode via device manager property pages is added.
 - LowLatency mode is enabled by default for baud-rates <= 50 Kbps.
 - Updated Set/Clr RTS/DTR logic in init and createfile dispatch so that it is on par with the standard uart driver.
 - WideMode support via ioctls calls is added for XR21B1411.
 - Break is turned off when the port is closed by the application, to be in sync with standard driver.
 - Improper state of TxHolding is fixed by updating interrupt endpoint logic. 


Revision History (Rev. 1.6 to 1.7):
 - IOCTL Support for enabling/disabling wide mode is added.
 - Support for turning on/off break is added.
 - LSR status is generated and is processed for any errors.
 - Endpoints are reset if there are any endpoint errors like stalled or halted.
 - Write Timeout logic is fixed and transmit empty event (SERIAL_EV_TXEMPTY) is implemented.
 - Cancelling and freeing of urbs are done in remove-device rather in closing of the ports to fix certain issues.

Revision History (Rev. 1.5 to 1.6):
 - Creating Symbolic link has been updated. This makes sure the Com is opened without any failure 
   even after the device is unplugged and plugged back.
 - Surprise removal portion is updated to avoid some potential issues when the port is closed 
   after the device is unplugged.

Revision History (Rev. 1.4 to 1.5):
 - Support for custom VID/PID - If OEMs want to use xrusbser.sys as is, they need to make sure
   XR21v1410/1412/1414 has even DID and XR21B1411 has odd DID. Otherwise different registers
   are programmed and the operation can not be guaranteed.
 - Fixed the bug that would have crashed the system if the driver is loaded for a phantom device 
   that was not uninstalled/installed properly.
 - IOCTL_SERIAL_GET_MODEMSTATUS now returns the live status of GPIO (reverted back to 1.2 logic). 

Revision History (Rev. 1.3 to 1.4):
 - Support for XR21B1411.
 - WriteTimeout is implemented.

Revision History (Rev. 1.2 to 1.3):
 - Improved data throughput to approximately 9Mbps
 - Fixed default state of RTS# and DTR# pins
 - Fix the usb 2.0 hub issue	
 - Changes in calculating serialstate in interrupt endpoint.