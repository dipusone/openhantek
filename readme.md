# OpenHantek [![Build Status](https://travis-ci.org/OpenHantek/openhantek.svg?branch=master)](https://travis-ci.org/OpenHantek/openhantek) [![Build status](https://ci.appveyor.com/api/projects/status/9w4rd5r04ufqafr4/branch/master?svg=true)](https://ci.appveyor.com/project/davidgraeff/openhantek/branch/master)
OpenHantek is a free software for Hantek (Voltcraft/Darkwire/Protek/Acetech) USB digital storage oscilloscopes based on HantekDSO and has started as an alternative to the official Hantek DSO software.

Supported operating systems:
* Linux
* MacOSX
* Windows (You need to download the [WinUSB driver files](http://libusb-winusb-wip.googlecode.com/files/winusb%20driver.zip) and customize the inf file for your device yourself at the moment)

<img alt="Image of main window" width="350" src="doc/screenshot_mainwindow.png">
<img alt="Image of main window" width="350" src="doc/screenshot_mainwindow_win.png">

Supported hantek devices:
* DSO2xxx Series
* DSO52xx Series

## Install prebuilt binary
Navigate to the [Releases](https://github.com/OpenHantek/openhantek/releases) page 

## Building OpenHantek from source
You need the following packages, to build OpenHantek from source:
* CMake 3.5+
* Qt 5.3+
* FFTW 3+ (prebuild files will be downloaded on windows)
* libusb 1.x (prebuild files will be used on windows)

For debian based systems (Ubuntu, Mint) install named requirements like this:
> apt-get install g++ cmake qttools5-dev qttools5-dev-tools libfftw3-dev binutils-dev libusb-1.0-0-dev

For rpm based distributions (Fedora) use this command:
> dnf install cmake gcc-c++ qt5-qtbase-gui qt5-qttools-devel qt5-qttranslations fftw-devel binutils-devel libusb-devel

For MacOSX use homebrew
> brew update <br>
> brew install libusb fftw qt5;

After you've installed the requirements either run **cmake-gui** or run the following commands inside the directory of this package:
> mkdir build <br>
> cd build <br>
> cmake ../ <br>
> make -j4 (for 4 concurrent compile jobs) <br>
> make install (optional, for installing only)

For MacOSX, the cmake command in the previous command list must include the directory where Qt5 is installed. Qt5 is installed in a directory with the same name of its version:
> brew info qt5
For example, if brew showed 5.7.0, the cmake command should be:
> cmake ../ -DCMAKE_PREFIX_PATH=/usr/local/Cellar/qt5/5.7.0

You can specify an install prefix when running cmake:
> cmake -DCMAKE_INSTALL_PREFIX=/usr

## Firmware
Your DSO does not store its firmware permanently -- the firmware has to be sent to the device each time it is connected. The `firmware` directory of this project contains the binary firmware extracted from Hantek's Windows drivers, and a udev rule to upload the firmware to the device automatically each time it is plugged in.

* You need binutils-dev autoconf automake fxload
* Install the `firmware/*.hex` files into `/usr/local/share/hantek/`.

> mkdir -p /usr/local/share/hantek <br>
> cp -r firmware/*.hex /usr/local/share/hantek/

* Install the `firmware/90-hantek.rules` file into `/etc/udev/rules.d/`.

> cp firmware/90-hantek.rules /etc/udev/rules.d/

* install fxload (fxload is a program which downloads firmware to USB  devices  based on AnchorChips EZ-USB, Cypress EZ-USB FX, or Cypress EZ-USB FX2 microcontrollers.)

> apt-get install fxload

* Add your current user to the **plugdev** group.

> usermod -a -G plugdev {user id}

## For 6022BE
You can adjust samplerate and use software triggering for 6022BE.
   - Support 48, 24, 16, 8, 4, 2, 1 M and 500, 200, 100 k Hz samplerates with modded firmware by [jhoenicke](https://github.com/rpcope1/Hantek6022API) 
   - Support software trigger by detecting rising or falling edge of signal. Use software trigger item on the trigger menu. For trigger level, adjust left arrow on the right-side of the graph.
   - Note that I dropped first 1000 samples due to unstable/unusual reading.
   - Fix triggering to generate a steady drawing and Make samplerate adjust to chosen timebase by [KimBP](https://github.com/KimBP/openhantek).
   - Fix bug and add color settings for printing.

## Contribute
Please use Github Issues to report any problems or enhancements or send us pull requests. Some random notes:
   - Read [how to properly contribute to open source projects on GitHub][10].
   - Use a topic branch to easily amend a pull request later, if necessary.
   - Write [good commit messages][11].
   - Squash commits on the topic branch before opening a pull request.
   - Use the same coding style and spacing.
   - Open a [pull request][12] that relates to but one subject with a clear title and description
     
[10]: http://gun.io/blog/how-to-github-fork-branch-and-pull-request
[11]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[12]: https://help.github.com/articles/using-pull-requests

## Other open source software
* [SigRok](www.sigrok.org)
* [Software for the Hantek 6022BE/BL only](http://pididu.com/wordpress/basicscope/)
