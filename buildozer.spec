[app]
title = Fizrenkli
package.name = fizrenkli
package.domain = org.kicijikshazada

# Siziň esasy .py faýlyňyz
source.dir = .
source.main = fizrenkli.py

version = 0.1

# Talap edilýän kitaphanalar 
# requirements = python3,kivy,pyjnius@https://github.com/kivy/pyjnius/archive/master.zip
requirements = python3,kivy,pyjnius,requests,certifi,openssl
orientation = portrait
fullscreen = 1

# APK-nyň içine giriziljek faýllar
source.include_exts = py,png,jpg,kv,atlas

# Içki meýletin sazlamalar
#osx.python_version = 3
#osx.kivy_version = 1.9.1

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# Android API
android.api = 31
android.minapi = 21

# SDK / NDK
android.sdk = 31
android.ndk = 21e

# Arhitekturalar
# android.archs = arm64-v8a,armeabi-v7a
android.archs = armeabi-v7a

# SDL2 boýunça täze gurluş
android.bootstrap = sdl2
