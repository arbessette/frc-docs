2027 Robot Overview
===================

The main change for 2027 is the move to Systemcore. Start there when planning
your electronics layout and updating an existing robot.

Systemcore
----------

*FIRST* has confirmed that Systemcore is required for the 2027 season. Each
team will receive a 4 GB unit in the season-specific box of the Kickoff Kit.

The production hardware has changes from the original alpha units, including
power and CAN connectors. Systemcore ships with power input cables; the
Black Tote includes Molex-SL cables and parts. Check which hardware you have
before following an older diagram or video.

See `FIRST's Systemcore update
<https://community.firstinspires.org/2026-systemcore-pricing-and-availability>`_
for the announcement and `WPILib's Systemcore introduction
<https://docs.wpilib.org/en/latest/docs/software/systemcore-info/systemcore-introduction.html>`_
for the controller overview.

Preparing your robot
--------------------

* Plan mounting and access for the controller, power distribution, radio,
  motor controllers, and wiring.
* Record the components and connections you intend to use.
* Check the manufacturer's instructions for each device and cable.
* Follow :doc:`../zero-to-robot/returning` for the software and controller
  update sequence.

The :doc:`older wiring walkthrough
<../zero-to-robot/step-1/basic-robot-wiring>` and CAN examples use a roboRIO.
Use them as references for that hardware; Systemcore connections need their
own instructions.

Kitbot and competition resources
--------------------------------

Use :doc:`../zero-to-robot/step-1/kitbot-starterbot-assembly` for official
assembly resources. Check :doc:`../competition/index` for season documents
before preparing for inspection.

Software updates
----------------

The 2027 software is still being developed. Use a matching WPILib release,
Driver Station, and Systemcore image. Check the
`2027 changelog
<https://docs.wpilib.org/en/latest/docs/yearly-overview/yearly-changelog.html>`_
and `known issues
<https://docs.wpilib.org/en/latest/docs/yearly-overview/known-issues.html>`_
for the release you are using.

Updated October 14, 2026, using the linked FIRST and WPILib documentation.
