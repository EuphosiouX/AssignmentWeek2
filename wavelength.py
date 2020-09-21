#Ask the user for the speed
speed = input('The speed (m/s): ')
Speed = float(speed)

#Ask the user for the frequency
freq = input('The frequency (Hz): ')
Freq = float(freq)

#To calculate the wavelength
wavelength = Speed/Freq

#Shows the output
print('The wavelength (m):',wavelength)
