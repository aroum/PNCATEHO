The Paintbrush
A small keyboard design for those who cannot or prefer not use 'traditional' keyboard designs.

This project aims to create a small keyboard design that is adaptable and flexible. Especially for those with disabilities, those who cannot type on traditional keyboads and those that prefer not use traditional keyboards.

The current version of The Painbrush is version 4. 

More information about The Paintbrush is available at https://github.com/artseyio/thepaintbrush


When compiling this keyboard you must specify if you are compiling the righty or lefty version. 

for example: 
	qmk compile -kb paintbrush/righty -km artsey_righty
	qmk compile -kb paintbrush/lefty -km artsey_lefty
or
	make -j 1 paintbrush/righty:artsey_righty
	make -j 1 paintbrush/lefty:artsey_lefty