# project_examples
This repo is to show any projects that I have worked on that is not company internal. 

# MonitorparityScrubber
For some context on this python script, when I had first started at Microsoft I was tasked with comparing all of our monitors between 2 isolated environments. Using a application I was able to pull all the current monitors in the environment. There are hundreds of monitors in these environments and originally I had to get the list of monitors generated go to the other environment and see if that monitor existed in that environment. It was a lot of manual toil. So I created this script that would look at the list from an excel file that was the monitors from one enviroment and cross reference the list generated. If there were any monitors that was not listed as being in our environment (AirGap) they would get marked and a exported list would be generated. So now we can easily know of the monitors that did not exist in our environment and make sure to follow up with our service teams and get reasoning on why these monitors were not in the AirGap environment. 

This was before I was embedded into the service team that allows to more directly fix this problem now where I am creating metrics that will go towards a monitor and alert us directly when there are disparities between environments. 
