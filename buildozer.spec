[app]
title = The Turning Tower
package.name = turningtower
package.domain = org.gmi.turningtower
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,wav
version = 2.0.0

# Kivy-specific requirements for your game script
requirements = python3,kivy==2.3.0,certifi

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
