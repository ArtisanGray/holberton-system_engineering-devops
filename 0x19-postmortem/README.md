-- ISSUE OCCURRED 8:00 PM CDST SEPT 29 2021, RESOLVED 10:00 PM CDST SEPT 29 2021 --
-- ISSUE CAUSE: RENDERING GLITCH AFFECTING REGIONALIZED CHUNKS IN MINECRAFT SERVER OVERWORLD BY 'DESTRUCTION' SCRIPT
-- RESOURCES/CLIENTS AFFECTED: 3 clients, total software failure --

-- TIMELINE --
- issue was detected around 8pm cdst.
- a client reported repeating server overflow errors upon chunk loading of a specific region.
- It was quickly reduced to block state changes created by a ai script (an attack of sorts). The change affected an area that shouldn't have been and created inconsistencies with world generation.
- originally, it was thought that an overflow error meant the system ran out of memory, but that is not the case. In some function, a fail case was triggering its handler in an infintismal way, causing the system to close itself before too much hang occurred.
- incident was escalated towards the owner, who had administrative controls over the system.
- incident was ruled as a problem with the error handling in said function, and to avoid any triggerig of it, a .json/.toml file was edited to prevent spawning of the mob that used AI script.

regarding fixing the root issue, the steps taken were as follows;

A setup script that managed a batch job had to be stopped, otherwise it would restart and reinitialize its resources, resulting in the fatal error again.
The server log needed to be read through to find the error that caused the crash, needing an outside text editor to do so.
The error hierarchy was kneaded through until the root file was found - a file in a folder relating to pathfinding scripts for a monster (dragon) and its attacks, one of which being an ice breath attack.
The function of the ice breath attack was to directly manipulate blocks its breath collided with to change in state to a 'frozen' counterpart, the problem being that it only affected 'default' blocks, none added by user modification.
This caused an error handler to trigger and try to refresh the state of the block, but no available state existed for it. This was only found after the error was replicated again, with I noting it being a consistent occurrence.
A quick solution was needed, but as i had no formal experience with Java or the codebase that was being used for the script, it was ruled that to get everything back to working order the entity that used the script would be cut off from the source.
Luckily, there are configuration files in the style of a JSON object that enables various attributes of modifications like the one that contained the entity. A line was added to the configuration file to disable spawning of the entity and the server was reinitialized, an all was well.
