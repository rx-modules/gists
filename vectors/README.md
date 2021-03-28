# Working with vectors and arrows

*This README.md uses [lectern](https://github.com/mcbeet/lectern#lectern-scripts) to compile into a valid datapack!*

This article will talk about manipulating vectors in Minecraft. This often becomes very helpful when working with arrows or entities with `Motion`!

Do note, I do talk about a bit of trigonometry here, but do not fret if you aren't super familiar with the subject! You should be able to be a *master manipulator of arrows* without needing any trig background, though you might learn a thing or two ;).

## Preamble

For this article, each segment of code will be organized in a singular function like `vect:attempt_1`. Running any attempt will loop itself so that you can try the different examples. To stop the looping, just run `vect:stop_loops`.

## Intro

If you've ever tried to work with altering an arrows path, you might have ran into a specific problem. For this example, let's try to make **all arrows fly towards the nearest player**. The first attempt might be to simply face the arrow towards the nearest player. Surely, this is the simplest solution and should work in one command!

<!-- @function vect:attempt_1 -->
```
execute as @e[type=arrow] at @s facing @p eyes run tp @s ~ ~ ~
```

<!-- 
This addons to the above function so that it loop itself
It also, stops other loops

@function(appends) vect:attempt_1
function vect:stop_loops
schedule function vect:attempt_1 1t
-->

To try this, run `function vect:attempt_1` and spawn a skeleton near you. You'll notice that the arrows shot don't behave as you expect them and it might even look a bit glitchy.

What's happening is that you are completely ignoring the `Motion` vector of the arrow entity! The arrow does not go in the direction it's facing, but rather, it faces in the direction it is going. Rather than changing the motion, you are changing the rotation which just makes the arrow flop back and forth as it flies through the arrow. In reality, you want to change the actual **trajectory** of the arrow by adjusting the `Motion` vector.

## The `Motion` Vector

*If you are familiar with this concept, you can skip to the next one :)*

All entities in Minecraft have a fancy vector called `Motion` which determines in what direction and how fast the entity is moving (essentially your velocity vector). You can read this pretty simply via `/data get entity <entity> Motion`. Try reading your player's velocity as you are falling via that command! You'll notice an output of 3 (seemingly long) numbers that look somewhat like `[0.0, -0.6, 0.0]`. This means that you are not moving on the `x` (the first number) and on the `z` axis, but you are moving downwards on the `y` axis, aka gravity.

> Note the long numbers are just really long decimals, Minecraft stores each component as a type of number called a `double` which essentially allows Minecraft to use very precise decimals to determine your movement.

In our `Motion` vector, we store how fast you are moving on the `x` axis, `y` axis, and `z` axis seperately. If we combine these numbers, we can determine in what direction we are moving and how fast we are. *Note that negative numbers just mean that you are moving backwards instead of forwards*.

Minecraft allows us to **set** these numbers on entities as well via the `/data modify` command. For example, let's *fling* a skeleton in the air:

```
data modify entity @e[type=skeleton, sort=nearest, limit=1] Motion set value [1.0d, 1.0d, 1.0d]
```

This command will apply `[1.0d, 1.0d, 1.0d]` this vector of motion on the skeleton *flinging* it through the air, with gravity eventually pulling it down.

### Vector Components

![pic](http://scienceres-edcp-educ.sites.olt.ubc.ca/files/2012/10/sec_phys_vectors_vectorComponents-940x705.jpg)


### Why do we care?

Our original goal is to take an arrow and have it *seek* towards the nearest player. To do this, rather than trying to have the arrow **face** the nearest player, we'll change the arrow to move **towards** the nearest player, aka, adjust the `Motion` of that arrow so that it flies towards the player.

You can imagine, we can set the `Motion` of our arrow so that it flies towards our player similar to how we flung the skeleton in the air.

## Arrow Manipulation 101: Helper Entities




<details>

<summary>Boilerplate for `lectern`</summary>

`@function vect:load`
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
