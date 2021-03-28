# Calculating Distance / Magnitude

*This README.md uses [lectern](https://github.com/mcbeet/lectern#lectern-scripts) to compile into a valid datapack!*

This method of calculating distance utilizes some facts about vectors making it super easy to implement in Minecraft.

## Resource // How to use

If you are just interested in a quick utility you can easily grab [this file](dist.mcfunction) or grab a datapack from the Github [releases](https://github.com/rx-modules/gists/releases) tab.

This script is pretty easy to use. It takes an input positional context as the starting point and input entity context as an ending point. Optionally, you can provide a vector in `storage` by setting `temp: dist.vector` to calculate any vector's magnitude (like `Motion` for velocity).

The output is in `$out temp` scaled by 1000 (for precision).

Assuming the file is located at `dist:calc` just try the following examples in chat (or run `function dist:example`)!

* This will calculate your distance from origin.
	<!-- @function dist:example -->	

	```
	execute positioned 0.0 0.0 0.0 run function dist:calc
	tellraw @a ["dist from origin: ", {"score": {"name": "$out", "objective": "temp"}}]
	```

* This will calculate the velocity of entity `@s`
	<!-- @function(append) dist:example -->

	```
	data modify storage temp: dist.vector set from entity @s Motion
	execute positioned 0.0 0.0 0.0 run function dist:calc
	tellraw @a ["velocity: ", {"score": {"name": "$out", "objective": "temp"}}]
	```
 
* This will measure the distance between two players
	<!-- @function(append) dist:example -->

	```
	execute at rx97 as vdvman1 run function dist:calc
	tellraw @a ["dist: ", {"score": {"name": "$out", "objective": "temp"}}]
	```

## The Math // How it works!

The base idea revolves around the fact that for any vector, *v*, the unit vector of *v* multiplied by the magnitude of *v* is equivalent to *v*. Therefore, we can easily calculate the magnitude by dividing *v* by the unit vector!

In this example image, vector **a**'s magnitude is 2.5 which can be seen as 2.5 * **a-hat** (the unit vector):

![vector-image](https://www.mathsisfun.com/algebra/images/vector-unit-scale.gif)

In terms of minecraft, all we have to do is take a component of a vector, like `Pos[0]` and divide by the unit-vector's cooresponding component.

To simplify, we can focus on just taking the magnitiude of a `Motion` vector.

<!--
Summon entity if it doesn't exist, not important

@function(append) dist:velocity
execute unless entity b5feab18-60ed-5ffd-b394-d71674d85bf6 run summon minecraft:area_effect_cloud ~ ~ ~ {Age:-2147483648,Duration:-1,WaitTime:-2147483648, UUID:[I;-1241601256,1626169341,-1282091242,1960336374]}
-->

First, we can set the `Pos` tag of our helper entity to the `Motion` of entity `@s`.

<!-- @function(append) dist:velocity -->

```
data modify entity b5feab18-60ed-5ffd-b394-d71674d85bf6 Pos set from entity @s Motion
```

Then, we can store the x component of our vector. We scale this up by 100,000 since later on we'll divide it by a number scaled by 100 (leaving us w/ a total scale of 1000).

<!-- Init $component
	`@function(append) dist:velocity`

	```
	scoreboard players set $component temp 0
	```
-->

<!-- @function(append) dist:velocity -->

```
execute store result score $velocity temp run data get entity @s Motion[0] 100000
```

<!--
Handle x, y and z

@function(append) dist:velocity

execute if score $velocity temp matches -10..10 run scoreboard players set $component temp 1

execute if score $component temp matches 1 store result score $velocity temp run data get entity @s Motion[1] 100000
execute if score $velocity temp matches -10..10 run scoreboard players set $component temp 2
execute if score $component temp matches 2 store result score $velocity temp run data get entity @s Motion[2] 100000
execute if score $velocity temp matches -10..10 run scoreboard players set $component temp -1
execute if score $component temp matches -1 run scoreboard players set $velocity temp 0
-->

Now, we can find our unit vector. To do this, we position outselves at the world origin (`0.0 0.0 0.0`), facing our helper entity (who is at the end point of our vector), and tp the helper entity 1 block in the direction of our vector (where it is point to). Getting `Pos[0]` will get the x component of our vector (scaled by 100).

<!-- @function(append) dist:velocity -->

```
execute positioned 0.0 0.0 0.0 as 6ded8fee-a099-56cd-9bdf-d92aa7bd8d5e facing entity @s feet run tp @s ^ ^ ^1
execute store result score $unit temp run data get entity 6ded8fee-a099-56cd-9bdf-d92aa7bd8d5e Pos[0] 100
```

<!--
Handle y and z unit vectors

@function(append) dist:velocity
execute if score $component temp matches 1 store result score $unit temp run data get entity 6ded8fee-a099-56cd-9bdf-d92aa7bd8d5e Pos[1] 100
execute if score $component temp matches 2 store result score $unit temp run data get entity 6ded8fee-a099-56cd-9bdf-d92aa7bd8d5e Pos[2] 100
-->


Lastly, dividing our x component from the `Motion` vector, `$velocity` by our unit vector, `$unit` will get us the magnitude of our vector (scaled by 1000).

<!-- @function(append) dist:velocity -->

```
scoreboard players operation @s velocity /= $normal_x temp
```

Note that this example only looks at the x component. If the x component were 0, we'd also want to look at the y and z components. You can take a look at `dist:velocity` in the generated datapack for a complete example.

<details>

<summary>Boilerplate to glue the datapack</summary>

[`@function dist:calc`](dist.mcfunction)

`@function dist:load`
```
scoreboard objectives add temp dummy
forceload add 0 0
```

`@function_tag minecraft:load`
```
{
	"values": ["dist:load"]
}
```

</details>

## Endnote

@vdvman1 came up with this concept in the mcc discord so it was pretty neat to throw this together. Also, this README.md is 10x lengthier than needs to be but I wanted to try out lectern as a way of writing cool articles!