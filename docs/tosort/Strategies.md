# Strategies

This file aims to have some guidelines for strategies to make work easier.

## Hisotry of issues

It is sad to say but I am not able upgrade personal systems as used to. In many cases I think that reinstall everything will solve problems.
But this is not easy as well as I need fully working system every day. 

One of way is to start using some intermidiate solutions, so this file should help me as much as possble.

## Issues

### 001 - PIP - pip install -U pip - breaks PIP

This is not easy to solve - as there is some restrictions on Main system and fully upgrading PIP is no longer valid.
Solution - Start using Vagrant (VM) for upgrading images. Why VM and not container (VM can run containers, but VM can have
much updated packages) - so this will allow develop / build / run (and if required use containers much easier).
