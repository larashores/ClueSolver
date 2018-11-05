# Installing Boost Python for mingw-64

Installing Boost Python for 64 bit Windows turned out to be incredibly difficult and took days to get working. These instructions should hopefully clear up that process. This guide is for Boost 1.67.0 and Python 3.7.0 but should hopefully be valid for any recent versions.

1. Download required files:

    * [boost_1_67_0.zip](https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.zip)
    * [x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z/download)
    * [python-3.7.0-amd64.exe](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe)
    
2) Extract `boost_1_67_0.zip` to a directory and add it to the system PATH
    * eg. Extract to `C:\boost_1_67_0` and add `C:\boost_1_67_0` to path
    
3) Copy the file `[boost_directory]\tools\build\example\user-config.jam` to your user directory which can be retrieved at `%HOMEDRIVE%%HOMEPATH%`
    * eg. Copy the file `C:\boost_1_67_0\tools\build\example\user-config.jam` to `C:\Users\username\user-config.jam`
    
4) Edit the last line to read
  
   ```
   using python : 3.7 : [python_install_dir]\\python.exe : [python_install_dir]\\include : [python_install_dir]\\libs ;
   ```

   Take care to escape any colons or backslashes. Make sure to leave spaces between the option and the last semicolon

5) Extract contents of `x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z` to a directory and add `mingw64\bin` to system PATH
    * eg. Extract to `C:\mingw64` and add `C:\mingw64\bin` to path
    
6) Run `python-3.7.0-amd64.exe` and install python to a directory
    * eg. Install to `C:\python37`
    
7) Open the file at `[python_install_directory]\include\pyconfig.h`
    * eg. Open `C:\python37\include\pyconfig.h`

8) Delete line 234 which is:
   
   ```
   #define hypot _hypot
   ```

9) Delete lines 195-199 which are:
   
   ```
   /* VS 2010 and above already defines hypot as _hypot */
   #if _MSC_VER < 1600
   #define hypot _hypot
   #endif
   ```

10) Save the file

11) Open a command prompt (possibly as adminstrator) and go to the boost install directory
    * eg. `cd C:\boost_1_67_0`

11) Run  `.\bootstrap.bat gcc`

12) Run the command `.\b2 --build-dir=[build_directory] --stagedir=[library_location] --toolset=gcc --build-type=complete --with-python -j[number_of_logical_cores] address-model=[32_or_64]`

    * eg (64 bit). `.\b2 --build-dir="boost-build\x64" --stagedir="stage\x64" --toolset=gcc --build-type=complete --with-python -j8 address-model=64`

    * eg (32 bit). `.\b2 --build-dir="boost-build\x86" --stagedir="stage\x86" --toolset=gcc --build-type=complete --with-system -j8 address-model=32`
  
    Both of these commands could be run if you want to build for both 32bit and 64bit Windows
    
That's it! That should hopefully get everything working. For an example on how to use this with CMake check out the [CMakeLists.txt](https://github.com/vinceshores/ClueSolver/blob/master/CMakeLists.txt) file for this project
