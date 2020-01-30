# Tower Defense Game
## Git protocol
1. Get the latest master:
    * first, checkout to master: `git checkout master`
    * then, get the data from the remote repo `git fetch`
    * move to working directory `git pull`
    * use `git status` to see what branch you're on and if you're behind or not. If it says you're `x commits behind master` or something then make sure to **fetch** and **pull**.
2. Move to subsystem branch, or if it already exists, just checkout to it.
    * doesn't exist > `git checkout -b <branch-name>`
    * does exist > `git checkout <branch-name>`
3. Do the work you need to do.
4. Update and push to localrepo using `git add . . .`, `git commit . . .` and `git push -u origin <branch-name>`
5. Go to <a href="https://github.com/veggiebob/tower-defense-pygame">the repo</a> and make a **pull request** (no comments needed)
6. Once it has been **reviewed** and **merged**, repeat from step 1.

This image is helpful:
![git command flow diagram](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2016/11/Git-Architechture-Git-Tutorial-Edureka-2-768x720.png)

## Links
> find todos, subsystems, leads: <a href="https://docs.google.com/spreadsheets/d/1rseG0xnOPBIf_O8NDjFT2qBSwP6-5G6BxBxhWZ3Hecs/edit?usp=sharing">subsystem sheet</a>  
> <a href="https://docs.google.com/document/d/1AFCMBRD75YpZa4AAXGGq73lxEBG0xS42JzzpD-Aply0/edit?usp=sharing">rough outline</a>  
> <a href="https://github.com/veggiebob/tower-defense-pygame">github link</a>

## Other
* helpful projects:
  * path (these could probably be pretty easily converted from js):
    * <a href="https://www.khanacademy.org/computer-programming/spline-interactive/5417132445892608">spline generation</a>
    * <a href="https://www.khanacademy.org/computer-programming/working-subdivision/6372348936224768"> subdivided line</a>