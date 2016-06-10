#These and other macros are documented in
#../droid-configs-device/droid-configs.inc
%define device grouper
%define vendor asus
%define vendor_pretty Asus
%define device_pretty Nexus 7
%define dcd_path ./
#Adjust this for your device
%define pixel_ratio 2.0
#We assume most devices will
%define have_modem 0
%include droid-configs-device/droid-configs.inc
