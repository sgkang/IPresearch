.. _api_IPIntro:

.. include:: ../maxwell.tex

******************************
What is induced polarization ?
******************************

Induced polarization (IP) phenmenon is simply considered as dispersive electrical conductivity effect on electromagnetic (EM) response. There are few models including Cole-Cole and stretched exponential models. 
The mosted used application is direct current (DC)-IP application, and in this case IP phenomenon is typically considered as overvoltage response in on-time. A simple understanding of this phenomenon is following: polarization charge builds up on earth, which acts like a capacitor, and this impedes the current flow. Decreased ability of current flow can be considered as the lowered conductivity, which generates overvoltage response as shown below. 

.. figure:: ./figures/DCIPcurve.png
    :width: 400px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Overvoltage effect in DC-IP measurments.

This is a typical IP response for a specific geophysical application. For different EM application, IP phenomenon may induce different response from overvoltage effect. For instance, in airborne time domain EM data, which uses coincident loop system, those are negative values. 

Mechansims of IP
================

Constricity polarization
-------------------------

Membrane polarization
---------------------

Constriccity polarization
-------------------------

Electrode polarization
----------------------

Complex conductivity
====================
IP phenomenon in EM responses can be explained by complex conductivity model, which is frequency dependent. An often-used representation for complex conductivity in the frequency domain is the Cole-Cole model:

.. math :: 
	\sigma(\omega) = \sigma_{\infty} - \sigma_{\infty}\frac{\eta}{1+(1-\eta)(\imath\omega\tau)^c} = \sigma_{\infty} + \triangle\sigma(\omega)
	:label: ColeCole

where :math:`\sigma_{\infty}` is the conductivity at infinite frequency, :math:`\eta` is the intrinsic chareability, :math:`\tau` is the time constant and :math:`c` is the frequency dependency. By applying inverse Fourier transform with time dependency, :math:`e^{\imath\omega t}`, we have

.. math :: 
	\begin{equation}
		\sigma(t) = \mathscr{F}^{-1}[\sigma(\omega)] = \sigma_{\infty}\delta(t) + \triangle\sigma(t)		
	\end{equation}
	:label: sigma_time

where :math:`\delta(t)` is Dirac delta function and :math:`\mathscr{F}^{-1}[\cdot]` is inverse Fourier transform operator. Assuming :math:`c=1`, we can easily evaluate :math:`\triangle\sigma(t)`, and this corresponds to Debye model. By evaluating inverse Fourier transform of :math:`\dsig(\omega)`, we have

.. math :: 
	\begin{equation}
		\dsig(t)  = -\siginf\frac{\eta}{(1-\eta)\tau}e^{-\frac{t}{(1-\eta)\tau}}u(t),		
	\end{equation}
	:label: deltasigma_time
where :math:`u(t)` is Heaviside step function. 

.. figure:: ./figures/FDandTDCole.png
    :width: 800px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Cole-Cole model in frequency domain and time domain. Left and right panel indicate frequency and time domain Cole-Cole model, respectively.



.. Maxwell's equations
.. ===================


.. .. math :: 
.. 	\begin{eqnarray}
.. 		\curl{\E} = -\imath\omega\B \\
.. 		\curl{\frac{1}{\mu} \B} - \J= \J_{s}
.. 	\end{eqnarray}
.. 	:label: maxwellF


Conceptual model
================

Consider Maxwell's equations in time domain:

.. math :: 
	\begin{equation}
		\curl{\e} = -\frac{\partial \b}{\partial t}
	\end{equation}
	:label: total_farad

.. math :: 
	\begin{equation}
		\curl{\frac{1}{\mu} \b} - \j= \j_{s}
	\end{equation}
	:label: total_coulomb

where :math:`\e` is the electric field (`V/m`), :math:`\b` is the magnetic flux density (:math:`Wb/m^2`) and :math:`\mu` is the magnetic permeability (`H/m`). Here :math:`\j` is the conduction current. In the frequency domain the current density :math:`\J` is related to conductivity via :math:`\J(\omega) = \sigma(\omega)\E(\omega)` where :math:`\E` is the electric field. Substituting equation :eq:`ColeCole` yields:

.. math ::

	\begin{equation}
		\J(\omega) = \siginf\E(\omega)+\triangle\sigma(\omega)\E(\omega) =\siginf\E(\omega)+\vec{J}_a(\omega),
	\end{equation}

where :math:`\J^{\ a}(\omega)` is the anomalous current density.
Converting this relationship to time domain using a Fourier transform yields:

.. math ::
	\begin{equation}
		\j(t) = \sigma(t)\otimes \e(t)
	\end{equation}
	:label: ohmslaw1

where :math:`\otimes` indicates time convolution. For causal signals, which is defined when `t \ge 0`, convolution between `a(t)` and `b(t)` can be written as

.. math ::
	\begin{equation}
		a(t) \otimes b(t) = \int_0^t a(u) b(t-u) du.
	\end{equation}
	:label: convolution

That is the current density depends upon the previous history of the electric field. Substituting equation :eq: `sigma_time` yields:

.. math ::
	\begin{equation}
		\j(t) = \siginf\e(t) + \dsig(t)\otimes\e(t) = \siginf\e(t) + \j^{\ a}(t),
	\end{equation}
	:label: ohmslaw2
where :math:`\j^{\ a}(t) = \dsig(t)\otimes\e(t)`.

As an example consider a chargeable block with the complex conductivity that is subjected to a constant electric field, :math:`\e^{ss}` at t = 0, and it does not change due to a chargeable body thus :math:`\e(t) = \e^{ss}u(t)`. 

.. figure:: ./figures/ChargeableBlock.png
    :width: 400px
    :align: center
    :alt: alternate text
    :figclass: align-center

    A chargeable block with the complex conductivity, which is subjected to a constant electric field.

Due to this, the first term in equation :eq:`ohmslaw2` can be considered as the current density if there were no polarization effects; the second term are the polarization currents. In our system where :math:`\e` is constant, those can be respectively considered as the fundamental current, :math:`\j^{F}` and the IP current :math:`\j^{IP}`, which is the same term as :math:`\j^{\ a}`. By using Cole-Cole model with :math:`c=1`  and evaluating convolution in the anomalous current density we have

.. math ::
	\begin{equation}
		\j^{IP}(t) = -\eta\siginf [1-e^{-\frac{t}{(1-\eta)\tau}}]\e^{ss} = -\peta(t)\siginf\e^{ss}		
	\end{equation}
	:label: IPdensity

with the final value at :math:`t = \infty` yielding :math:`\j^{\ a}=-\eta\siginf\e^{ss}=-\eta\j^F`, and thus :math:`\j = \siginf(1-\eta)\e^{ss}`. That is, the polarization is a fraction, :math:`\eta` of the fundamental current density, :math:`\j^F`, and is in the opposite direction to :math:`\j^F`. This mathematical representation  about anomalous current density in terms of Cole-Cole model agrees with Seigel's  result. Thus, we have total current:

.. math ::
	\begin{equation}
		\j(t) = \j^{F}(t) + \j^{IP}(t) = \siginf(1-\peta(t))\e^{ss},	  
	\end{equation}
	:label: ohmslaw3

where :math:`\peta(t) = \frac{\dsig(t)\otimes u(t)}{\siginf}`.
We can define an effective conductivity as

.. math ::
	\begin{equation}
		\sigma_{eff}(t) = \frac{\j(t)}{\e^{ss}} = \siginf(1-\peta(t)) = \siginf + \delta\sigma(t).		
	\end{equation}
	:label: sigeff

For :math:`t \rightarrow \infty`, :math:`\peta\rightarrow \eta` (the intrinsic chargeability) and :math:`\sigma_{eff} = \siginf(1-\eta)`, which is well used result.

Conversely, based on equation :eq:`sigeff`, we define an perturbed conductivity as

.. math ::
	\begin{equation}
		\delta\sigma(t) = -\siginf\peta(t) =\frac{\dsig(t)\otimes \e(t)}{\e^{ss}}
	\end{equation}
	:label: sigpert

Then we can rewrite equation :eq:`ohmslaw3` as

.. math ::
	\begin{equation}
		\j(t) = (\siginf + \delta\sigma(t))\e(t)
	\end{equation}

This is a fundamental statement of linearization in time domain electrical field IP (EIP)  and magnetic field IP (MIP) responses, since it allows us to expand Maxwell's operator in terms of :math:`\sigpert(t)` for each time channel. 

.. figure:: ./figures/Convolution_es.png
    :width: 800px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Convolution of time dependent conductivity (:math:`\sigma(t)`) and step-on electric field in x-direction.

