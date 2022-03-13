The flag is broken down into 3 pieces

To obtain the first piece: open the flag_1.wav file in Audacity. In its spectrogram image, you can find 3 coordinates:
45.4215N, 75.6972W
23.5880N, 58.3829E
27.7172N, 85.3240E


To obtain the second piece, there are 2 methods:
1. Open the flag_2.png file with WinRar and extract it, you can find the file good_job.pdf. At the final page of the pdf, you can find the next 3 coordinates.
2. Use binwalk (the solution to the riddle in the image), run this command: `binwalk --dd='.*' flag_2.png` then go to ./_flag_2.png.extracted/, rename the file 719E to 719E.rar, extract it and again you can see the good_job.pdf file.
The 3 coordinates are:
64.1814N, 51.6941W
44.4268N, 26.1025E
35.2802S, 149.1310E  


To obtain the final piece, open the flag_3 file in hexedit, or [here](https://hexed.it/). There you will find that the file extension is JFIF (an image file) but the header is altered abit. A bit of Googling shows that the correct first 4 bytes are FF D8 FF E0, simply change the header to that and rename the file to flag_3.jfif. Opening the file reveals the final 2 coordinates:
39.9334N, 32.8597E
59.3293N, 18.0686E


The 8 coordinates points to 8 countries:
Canada
Oman
Nepal
Greenland
Romania
Australia
Turkey
Sweden

The first letters of those are C, O, N, G, R, A, T, S
And the flag is f0rtn1ght{CONGRATS}