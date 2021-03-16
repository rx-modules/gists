# Calculating Distance / Magnitude

*This README.md uses [lectern](https://github.com/mcbeet/lectern#lectern-scripts) to compile into a valid datapack!*

This method of calculating distance utilizes some facts about vectors making it super easy to implement in Minecraft. The base idea revolves around the fact that for any vector, *v*, the unit vector of *v* multiplied by the magnitude of *v* is equivalent to *v*. Therefore, we can easily calculate the magnitude by dividing *v* by the unit vector!

## Resource

If you are just interested in a quick utility you can easily grab [this file](dist/dist.mcfunction) or grab the release datapack compiled from this 
