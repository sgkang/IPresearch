.. Induced Polarization documentation master file, created by
   sphinx-quickstart on Mon Mar  9 22:17:28 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Recovering distributed IP information from EM data
==================================================

The electrical conductivity of earth materials can be frequency dependent due to the build-up of charges that occur under the application of an electric field.  Effectively, the rock is electrically polarized. Polarization charges can accumulate whenever there is an electric field in a medium and so the transmitter can be a galvanic or inductive source. Although every measurments on time domain, based on the transmitting wavefore, electromagnetic (EM) response in time can be transformed to frequency domain so that we can have complex response, which has amplitude and phase. 

Currently, induced polarzation (IP) phenomenon EM data is broadly used in the areas including minining, ground water and oil and gas applications. Fundamental understanding of this phenomenon on laboratory scale has been throughly treated. However, extracting IP response on various types of EM data: galvanic / inductive / time / frequency to recover distribution of IP parameters has not been tackled yet. 

Therefore, for my PhD research, I clearly identify characteristics of IP responses in current EM systems. And decouple IP responses from the observation, to distinguish IP response embedded in the observation. For the restoration of distributed IP parameter, first I linearize IP response as a function of pseudo-chargeability. Natural next step is towards using non-linear kernel to restore instrinsic IP parameters from the earth. 

Contents
========

.. toctree::
   :maxdepth: 2

   ./IPtheory/api_IPIntro


Project Index & Search
======================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

