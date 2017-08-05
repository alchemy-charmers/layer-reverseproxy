# Overview

This charm implements the requires side of the [reverseproxy interface][reverseproxy]. This
allows you to request and configure a reverseproxy on a machine that doesn't
implemnt the interface.

# Usage

To deploy:

    juju deploy cs:~chris.sanders/reverseproxy --to 1
    juju add-relation reverseproxy haproxy

In the above example this charm is deployed to machine 1 and a relation is 
added to the [haproxy charm][haproxy].

# Configuration

See configuration options below.

# Contact Information

## Upstream Project Name

  - Code: https://github.com/chris-sanders/layer-reverseproxy
  - Bug tracking: https://github.com/chris-sanders/layer-reverseproxy/issues
  - Contact information: sanders.chris@gmail.com


[haproxy]: https://jujucharms.com/u/chris.sanders/haproxy
[reverseproxy]: https://github.com/chris-sanders/interface-reverseproxy
