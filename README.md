# YouTubeSkip
This code automatically skip adds and closes banner adds on YouTube (when possible).

The code performs the following tasks:
 - take a screenshot of the entire screen
 - compare each block of pixels in the screenshot to the reference images
 - find the block with the hightest similarity measure for each reference images
 - if the similarity measure of this block is above a threshold, the cursor is moved to this block and left-clock is pressed
