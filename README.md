# Kremepuff

## About

Kremepuff is a tool used to enroll users in the Fob All the Things project.  It
allows users to easily generate directions.  It can be used with or without the
[makerspace-auth][makerspace-auth] hardware.

## Setup

This application's dependencies can be installed using `pip` and the built-in
git submodule.

### Dependencies

Kremepull has the following dependencies:

#### [Makerspace-Auth][makerspace-auth]
Used for RFID handling (*Note*: It does not require the makerspace-auth
_hardware_ only the makerspace-auth software).

#### [python-escpos][python-escpos]
Used for receipt printer handling.

[makerspace-auth]: https://github.com/google/makerspace-auth
[python-escpos]: https://python-escpos.readthedocs.io/en/latest/

<!--
 vim: ts=2 sw=2 et tw=80 syntax=markdown
-->
