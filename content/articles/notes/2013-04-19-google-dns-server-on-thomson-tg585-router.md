Title: Configuring Google Public DNS servers on a Thomson TG585v7 router.
Date: 2013-04-19 21:00
Tags: routers, DNS, old-news, testing-pygments
Slug: google-public-dns-servers-on-a-thomson-tg585v7-router
Summary: Last night i wanted to change my router's DNS servers to utilize Google Public DNS and here's how i did it.

Have an oldish (?) Thomson TG585v7 router and last night i wanted to change it's DNS servers to utilize Google Public DNS, because this domains TLD wasn't yet resolving on my end only.

From <https://developers.google.com/speed/public-dns/>

> Google Public DNS is a free, global Domain Name System (DNS) resolution service, that you can use as an alternative to your current DNS provider.

Also, i have been meaning to try Google DNS and after some googling, found the answer here: <http://community.plus.net/library/dns/how-to-change-the-default-dns-servers-in-a-thomson-speedtouch-router/>.

So, i booted `telnet` and here we go.

First let's login
    
    :::console
    zemanel on victory at ~  telnet 192.168.1.254
    Trying 192.168.1.254...
    Connected to 192.168.1.254.
    Escape character is '^]'.
    Username : Administrator
    Password : *************
    ------------------------------------------------------------------------

                                 ______  Thomson TG585 v7
                             ___/_____/\
                            /         /\  7.4.3.2
                      _____/__       /  \
                    _/       /\_____/___ \  Copyright (c) 1999-2007, THOMSON
                   //       /  \       /\ \
           _______//_______/    \     / _\/______
          /      / \       \    /    / /        /\
       __/      /   \       \  /    / /        / _\__
      / /      /     \_______\/    / /        / /   /\
     /_/______/___________________/ /________/ /___/  \
     \ \      \    ___________    \ \        \ \   \  /
      \_\      \  /          /\    \ \        \ \___\/
         \      \/          /  \    \ \        \  /
          \_____/          /    \    \ \________\/
               /__________/      \    \  /
               \   _____  \      /_____\/
                \ /    /\  \    /___\/
                 /____/  \  \  /
                 \    \  /___\/
                  \____\/

    ------------------------------------------------------------------------
    _{Administrator}=>

and we're in. Now let's check the current DNS list

    :::console
    _{Administrator}=>:dns server route list
    DNS Server Entries:
      DNS server    Source    Label    Metric    Intf          State   Domain
      S 194.79.69.222                  0         Internet      UP      *
      S 195.23.129.126                 0         Internet      UP      *

For changing the entries, clearing the list and adding Google DNS entries is the Easy Way(c).

    :::console
      _{Administrator}=> dns server route flush
      _{Administrator}=> dns server route add dns=8.8.8.8 metric=0 intf=Internet
      _{Administrator}=> dns server route add dns=8.8.4.4 metric=0 intf=Internet
      _{Administrator}=> saveall

Just confirming the current list

    :::console
    _{Administrator}=>:dns server route list
    DNS Server Entries:
      DNS server    Source    Label    Metric    Intf          State   Domain
      S 8.8.8.8                        0         Internet      UP      *
      S 8.8.4.4                        0         Internet      UP      *

and we're good to go :) .

    :::console
      _{Administrator}=>exit
