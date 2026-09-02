



Error! No  
text of

Error! No text of specified style in  
document.

# Contents

|                                                                          |    |
|--------------------------------------------------------------------------|----|
| Foreword .....                                                           | 6  |
| 1 Scope.....                                                             | 7  |
| 2 References.....                                                        | 7  |
| 3 Definitions, symbols and abbreviations.....                            | 7  |
| 3.1 Definitions.....                                                     | 7  |
| 3.2 Symbols.....                                                         | 8  |
| 3.3 Abbreviations .....                                                  | 8  |
| 4 General.....                                                           | 9  |
| 4.1 Relationship between minimum requirements and test requirements..... | 9  |
| 4.2 Relay classes .....                                                  | 9  |
| 4.3 Regional requirements.....                                           | 9  |
| 5 Operating bands and channel arrangement.....                           | 10 |
| 5.1 General .....                                                        | 10 |
| 5.2 Operating bands.....                                                 | 10 |
| 5.3 Channel bandwidth.....                                               | 10 |
| 5.4 Channel arrangement.....                                             | 10 |
| 6 Transmitter characteristics .....                                      | 10 |
| 6.1 General .....                                                        | 10 |
| 6.2 Output power.....                                                    | 11 |
| 6.2.1 Maximum output power .....                                         | 11 |
| 6.2.1.1 Minimum requirement .....                                        | 11 |
| 6.2.2 Configured transmitted Power for backhaul link .....               | 11 |
| 6.2.2.1 Minimum requirement .....                                        | 12 |
| 6.3 Output power dynamics .....                                          | 12 |
| 6.3.1 Minimum output power .....                                         | 12 |
| 6.3.1.1 Minimum requirement .....                                        | 12 |
| 6.3.2 ON/OFF time mask and transmitter OFF power.....                    | 12 |
| 6.3.3 Power control.....                                                 | 13 |
| 6.4 Transmitted signal quality.....                                      | 13 |
| 6.4.1 Frequency error .....                                              | 13 |
| 6.4.1.1 Minimum requirement .....                                        | 13 |
| 6.4.2 EVM .....                                                          | 13 |
| 6.4.3 Time alignment error.....                                          | 13 |
| 6.4.4 DL RS power.....                                                   | 13 |
| 6.5 Unwanted emissions.....                                              | 13 |
| 6.5.1 Transmitter spurious emissions .....                               | 14 |
| 6.5.2 Adjacent Channel Leakage power Ratio (ACLR).....                   | 14 |
| 6.5.3 Operating band unwanted emissions.....                             | 14 |
| 6.5.3.1 Minimum requirements.....                                        | 14 |
| 6.6 Transmitter intermodulation.....                                     | 16 |
| 7 Receiver characteristics.....                                          | 16 |
| 7.1 General .....                                                        | 16 |
| 7.2 Reference sensitivity level .....                                    | 16 |
| 7.2.1 Backhaul link reference sensitivity.....                           | 16 |
| 7.2.1.1 Minimum requirement .....                                        | 16 |
| 7.2.2 Access link reference sensitivity .....                            | 16 |
| 7.2.2.1 Minimum requirement .....                                        | 16 |
| 7.3 Dynamic range .....                                                  | 17 |
| 7.3.1 Backhaul link maximum input level.....                             | 17 |
| 7.3.2 Access link Receiver Dynamic Range.....                            | 17 |
| 7.4 In-channel selectivity .....                                         | 17 |
| 7.4.1 Access link in-channel selectivity .....                           | 17 |
| 7.5 Adjacent Channel Selectivity (ACS).....                              | 17 |
| 7.5.1 Backhaul link Adjacent Channel Selectivity.....                    | 17 |
| 7.5.1.1 Minimum requirement .....                                        | 17 |

|                 |                                                                           |           |
|-----------------|---------------------------------------------------------------------------|-----------|
| 7.5.2           | Access link Adjacent Channel Selectivity.....                             | 18        |
| 7.6             | Blocking characteristics .....                                            | 18        |
| 7.6.1           | Backhaul link blocking characteristics.....                               | 18        |
| 7.6.1.1         | Minimum requirement .....                                                 | 18        |
| 7.6.2           | Access link blocking characteristics.....                                 | 19        |
| 7.6.3           | Blocking requirements for co-location.....                                | 19        |
| 7.7             | Receiver spurious emissions .....                                         | 20        |
| 7.8             | Receiver intermodulation .....                                            | 20        |
| 7.8.1           | Backhaul link receiver intermodulation .....                              | 20        |
| 7.8.1.1         | Minimum requirement .....                                                 | 20        |
| 7.8.2           | Access link receiver intermodulation .....                                | 20        |
| 8               | Access Performance requirement.....                                       | 21        |
| 8.1             | General .....                                                             | 21        |
| 8.2             | Performance requirements for PUSCH .....                                  | 21        |
| 8.2.1           | Requirements in multipath fading propagation conditions .....             | 21        |
| 8.2.2           | Requirements for UL timing adjustment.....                                | 21        |
| 8.2.3           | Requirements for HARQ-ACK multiplexed on PUSCH .....                      | 21        |
| 8.3             | Performance requirements for PUCCH.....                                   | 21        |
| 8.3.1           | DTX to ACK performance .....                                              | 21        |
| 8.3.2           | ACK missed detection requirements for single user PUCCH format 1a .....   | 21        |
| 8.3.3           | CQI missed detection requirements for PUCCH format 2 .....                | 21        |
| 8.3.4           | ACK missed detection requirements for multi user PUCCH format 1a .....    | 22        |
| 8.4             | Performance requirements for PRACH.....                                   | 22        |
| 8.4.1           | PRACH False alarm probability.....                                        | 22        |
| 8.4.2           | PRACH detection requirements .....                                        | 22        |
| 9               | Backhaul Performance requirement.....                                     | 22        |
| 9.1             | General .....                                                             | 22        |
| 9.2             | Demodulation of PDSCH (Cell-Specific Reference Symbols).....              | 22        |
| 9.3             | Demodulation of PDSCH (User-Specific Reference Symbols).....              | 22        |
| 9.4             | Demodulation of PDCCH/PCFICH .....                                        | 22        |
| 9.5             | Demodulation of PHICH.....                                                | 22        |
| 9.6             | Demodulation of PBCH .....                                                | 23        |
| 9.7             | Sustained downlink data rate provided by lower layers.....                | 23        |
| 9.8             | Demodulation of R-PDCCH .....                                             | 23        |
| 9.8.1           | R-PDCCH format without cross-interleaving .....                           | 23        |
| 9.8.1.1         | FDD .....                                                                 | 23        |
| 9.8.1.2         | TDD .....                                                                 | 25        |
| <b>Annex A:</b> | <b>Propagation models for relay demodulation requirements.....</b>        | <b>27</b> |
| A.1             | Propagation models for backhaul link .....                                | 27        |
| A.1.1           | Delay Profiles.....                                                       | 27        |
| A.1.1.1         | LOS between eNB and relay .....                                           | 27        |
| A.1.1.2         | NLOS between eNB and relay .....                                          | 27        |
| A.1.2           | Doppler Frequency.....                                                    | 28        |
| A.1.3           | MIMO Correlation Matrices .....                                           | 28        |
| A.2             | Multipath propagation fading conditions for access link.....              | 29        |
| <b>Annex B:</b> | <b>Reference Measurement Channel.....</b>                                 | <b>31</b> |
| B.1             | Reference measurement channels for R-PDCCH performance requirements ..... | 31        |
| B.1.1           | R-PDCCH format without cross-interleaving.....                            | 31        |
| B.1.1.1         | FDD .....                                                                 | 31        |
| B.1.1.2         | TDD.....                                                                  | 31        |
| B.2             | OCNG patterns for R-PDCCH performance requirements.....                   | 31        |
| B.2.1           | FDD.....                                                                  | 32        |
| B.2.1.1         | OCNG FDD pattern 1for R-PDCCH.....                                        | 32        |
| B.2.2           | TDD.....                                                                  | 32        |
| B.2.2.1         | OCNG TDD pattern 1for R-PDCCH .....                                       | 32        |

Annex C: Change history................................................................................................................................................ 34

# --- Foreword

This Technical Specification has been produced by the 3<sup>rd</sup> Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit:
  - 1 presented to TSG for information;
  - 2 presented to TSG for approval;
  - 3 or greater indicates TSG approved document under change control.
- y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.
- z the third digit is incremented when editorial only changes have been incorporated in the document.

# --- 1 Scope

The present document establishes the minimum RF characteristics and minimum performance requirements of E-UTRA Relay.

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
  - For a specific reference, subsequent revisions do not apply.
  - For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.
- [1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".
- [2] 3GPP TS 36.101: "User Equipment (UE) radio transmission and reception"
- [3] 3GPP TS 36.104: "Base Station (BS) radio transmission and reception"
- [4] ITU-R Recommendation SM.329-10, "Unwanted emissions in the spurious domain".
- [5] ITU-R Recommendation M.1545: "Measurement uncertainty as it applies to test limits for the terrestrial component of International Mobile Telecommunications-2000".

# --- 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [x] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [x].

**Access link:** Link for communication between Relay and UE.

**Backhaul link:** Link for communication between Relay and BS.

**Carrier:** The modulated waveform conveying the E-UTRA or UTRA physical channels

**Channel bandwidth:** The RF bandwidth supporting a single E-UTRA RF carrier with the transmission bandwidth configured in the uplink or downlink of a cell. The channel bandwidth is measured in MHz and is used as a reference for transmitter and receiver RF requirements.

**Channel edge:** The lowest and highest frequency of the E-UTRA carrier, separated by the channel bandwidth.

**In-band relay:** A Relay where the access link and backhaul link operates in the same operating band.

**Measurement bandwidth:** The bandwidth in which an emission level is specified.

**Occupied bandwidth:** The width of a frequency band such that, below the lower and above the upper frequency limits, the mean powers emitted are each equal to a specified percentage  $\beta/2$  of the total mean power of a given emission.

**RRC filtered mean power:** The mean power of a UTRA carrier as measured through a root raised cosine filter with roll-off factor  $\alpha$  and a bandwidth equal to the chip rate of the radio access mode.

NOTE 1: The RRC filtered mean power of a perfectly modulated UTRA signal is 0.246 dB lower than the mean power of the same signal.

**Transmission bandwidth:** Bandwidth of an instantaneous transmission from a UE or BS, measured in Resource Block units.

**Transmission bandwidth configuration:** The highest transmission bandwidth allowed for uplink or downlink in a given channel bandwidth, measured in Resource Block units.

## 3.2 Symbols

Void

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [x] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [x].

|         |                                                           |
|---------|-----------------------------------------------------------|
| ACLR    | Adjacent Channel Leakage Ratio                            |
| ACK     | Acknowledgement (in HARQ protocols)                       |
| ACS     | Adjacent Channel Selectivity                              |
| AWGN    | Additive White Gaussian Noise                             |
| BS      | Base Station                                              |
| CP      | Cyclic prefix                                             |
| CRC     | Cyclic Redundancy Check                                   |
| CW      | Continuous Wave                                           |
| DC      | Direct Current                                            |
| DFT     | Discrete Fourier Transformation                           |
| DTX     | Discontinuous Transmission                                |
| DwPTS   | Downlink part of the special subframe (for TDD operation) |
| EARFCN  | E-UTRA Absolute Radio Frequency Channel Number            |
| EPA     | Extended Pedestrian A model                               |
| ETU     | Extended Typical Urban model                              |
| E-UTRA  | Evolved UTRA                                              |
| EVA     | Extended Vehicular A model                                |
| EVM     | Error Vector Magnitude                                    |
| FDD     | Frequency Division Duplex                                 |
| FFT     | Fast Fourier Transformation                               |
| FRC     | Fixed Reference Channel                                   |
| GP      | Guard Period (for TDD operation)                          |
| HARQ    | Hybrid Automatic Repeat Request                           |
| HD-FDD  | Half- Duplex FDD                                          |
| ICS     | In-Channel Selectivity                                    |
| ITU-R   | Radiocommunication Sector of the ITU                      |
| LA      | Local Area                                                |
| MCS     | Modulation and Coding Scheme                              |
| OFDM    | Orthogonal Frequency Division Multiplex                   |
| OOB     | Out-of-band                                               |
| PA      | Power Amplifier                                           |
| PBCH    | Physical Broadcast Channel                                |
| PDCCH   | Physical Downlink Control Channel                         |
| PDSCH   | Physical Downlink Shared Channel                          |
| PUSCH   | Physical Uplink Shared Channel                            |
| PUCCH   | Physical Uplink Control Channel                           |
| PRACH   | Physical Random Access Channel                            |
| PSS     | Primary Synchronization Signal                            |
| QAM     | Quadrature Amplitude Modulation                           |
| QPSK    | Quadrature Phase-Shift Keying                             |
| RAT     | Radio Access Technology                                   |
| RB      | Resource Block                                            |
| RE      | Resource Element                                          |
| REFSENS | Reference Sensitivity power level                         |
| RF      | Radio Frequency                                           |
| RMS     | Root Mean Square (value)                                  |

|         |                                            |
|---------|--------------------------------------------|
| R-PDCCH | Relay Physical Downlink Control Channel    |
| RS      | Reference Symbol                           |
| RX      | Receiver                                   |
| RRC     | Root Raised Cosine                         |
| SNR     | Signal-to-Noise Ratio                      |
| SSS     | Secondary Synchronization Signal           |
| TA      | Timing Advance                             |
| TDD     | Time Division Duplex                       |
| TX      | Transmitter                                |
| UE      | User Equipment                             |
| UMTS    | Universal Mobile Telecommunications System |
| UTRA    | UMTS Terrestrial Radio Access              |
| UTRAN   | UMTS Terrestrial Radio Access Network      |
| WA      | Wide Area                                  |

# --- 4 General

## 4.1 Relationship between minimum requirements and test requirements

The Minimum Requirements given in this specification make no allowance for measurement uncertainty. The test specification defines Test Tolerances. These Test Tolerances are individually calculated for each test. The Test Tolerances are used to relax the Minimum Requirements in this specification to create Test Requirements.

The measurement results returned by the Test System are compared - without any modification - against the Test Requirements as defined by the shared risk principle.

The Shared Risk principle is defined in ITU-R M.1545 [5].

## 4.2 Relay classes

The Relay classes are defined based on the RF scenarios expected for the Relay access deployment, defined in terms of the Minimum Coupling Loss (MCL) between Relay and UE. The following definitions are used:

- High-CL Relay are characterised by requirements derived from outdoor Relay scenarios with a Relay to UE minimum coupling loss equals to 59 dB.
- Low-CL Relay are characterised by requirements derived from indoor Relay scenarios with a Relay to UE minimum coupling loss equals to 45 dB.

## 4.3 Regional requirements

Some requirements in the present document may only apply in certain regions either as optional requirements or set by local and regional regulation as mandatory requirements. It is normally not stated in the 3GPP specifications under what exact circumstances that the requirements apply, since this is defined by local or regional regulation.

Table 4.3-1 lists all requirements that may be applied differently in different regions.

**Table 4.3-1: List of regional requirements**

| Clause number | Requirement                           | Comments                                                                                                                        |
|---------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 5.2           | Operating bands                       | Some bands may be applied regionally.                                                                                           |
| 5.3           | Channel bandwidth                     | Some channel bandwidths may be applied regionally.                                                                              |
| 5.4           | Channel arrangement                   | The requirement is applied according to what operating bands in clause 5.5 that are supported by the BS.                        |
| 6.5.1         | Transmitter spurious emissions        | Some of the requirements references in this may be applied regionally. This is further detailed in TS 36.104 [3] subclause 4.3. |
| 7.6.3         | Blocking requirements for co-location | Some of the requirements references in this may be applied regionally. This is further detailed in TS 36.104 [3] subclause 4.3. |

# --- 5 Operating bands and channel arrangement

## 5.1 General

The channel arrangements presented in this clause are based on the operating bands and channel bandwidths defined in the present release of specifications.

NOTE: Other operating bands and channel bandwidths may be considered in future releases.

## 5.2 Operating bands

E-UTRA is designed to operate in the operating bands defined in Table 5.5-1 of TS 36.104 [3].

## 5.3 Channel bandwidth

Requirements in present document are specified for the channel bandwidths listed in Table 5.6-1 of TS 36.104 [3].

For the access link the manufacturer shall declare the channel bandwidths supported by the Relay.

The the backhaul link the Relay shall support the channel bandwidths denoted by "Yes" in Table 5.6.1-1 of TS 36.101 [2] for the supported operating band. Note 1 in Table 5.6.1-1 does not apply.

## 5.4 Channel arrangement

The channel spacing is specified in subclause 5.7.1 of TS 36.104 [3].

The channel raster is specified in subclause 5.7.2 of TS 36.104 [3].

Carrier frequency and EARFCN is specified in subclause 5.7.3 of TS 36.104 [3].

# --- 6 Transmitter characteristics

## 6.1 General

Unless otherwise stated, the requirements in clause 6 are expressed for a single transmitter antenna connector. In case of multi-carrier transmission with one or multiple transmitter antenna connectors, transmit diversity or MIMO transmission, the requirements apply for each transmitter antenna connector.

Unless otherwise stated the requirements in clause 6 shall apply for both the access link and backhaul link at all times, i.e. during the Transmitter ON period, the Transmitter OFF period and the Transmitter transient period.

## 6.2 Output power

The rated output power is the mean power level that the manufacturer has declared to be available at the antenna connector during the transmitter ON period. Two power classes are defined for relay access link and single power class is defined for relay backhaul link, where the rated output power shall be as specified in Table 6.2-2 and Table 6.2-3.

**Table 6.2-1: Void**

**Table 6.2-2: Relay access link rated output power**

| Access link Power class | Rated output power [dBm]                                                                                                                                                                   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power class 1           | $\leq +24$ (for one transmit antenna port)<br>$\leq +21$ (for two transmit antenna ports)<br>$\leq +18$ (for four transmit antenna ports)<br>$\leq +15$ (for eight transmit antenna ports) |
| Power class 2           | $\leq +30$ (for one transmit antenna port)<br>$\leq +27$ (for two transmit antenna ports)<br>$\leq +24$ (for four transmit antenna ports)<br>$\leq +21$ (for eight transmit antenna ports) |

**Table 6.2-3: Relay backhaul link rated output power**

| Backhaul link Power class | Rated output power [dBm]                                                                                                                  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Power class 1             | $\leq +24$ (for one transmit antenna port)<br>$\leq +21$ (for two transmit antenna ports)<br>$\leq +18$ (for four transmit antenna ports) |

NOTE: For coexistence with a victim base station a minimum MCL should be met in all scenarios. This is particularly relevant for use cases where relays are placed wall mounted or in rooftops. The value for this MCL is FFS.

### 6.2.1 Maximum output power

The maximum output power, of the Relay is the mean power level measured at the antenna connector during the transmitter ON period in a specified reference condition. The period of measurement shall be at least one sub frame (1ms)

#### 6.2.1.1 Minimum requirement

In normal conditions, the maximum output power shall remain within +2 dB and -2 dB of the rated output power declared by the manufacturer.

In extreme conditions, the maximum output power shall remain within +2.5 dB and -2.5 dB of the rated output power declared by the manufacturer.

In certain regions, the minimum requirement for normal conditions may apply also for some conditions outside the range of conditions defined as normal.

### 6.2.2 Configured transmitted Power for backhaul link

The Relay backhaul link is allowed to set its configured maximum output power  $P_{CMAX}$ . The configured maximum output power  $P_{CMAX}$  is set within the following bounds:

- $P_{CMAX} = \text{MIN} \{ P_{EMAX}, \text{PRAT} \}$
- $P_{EMAX}$  is the value given to IE *P-Max*, defined in TS36.331
- PRAT is the Relay rated output power specified in table 6.2.1-1 without taking into account the tolerance specified in the table 6.2.2.1-1

#### 6.2.2.1 Minimum requirement

The measured configured maximum output power  $P_{UMAX}$  shall be within the following bounds:

$$P_{CMAX} - T(P_{CMAX}) \leq P_{UMAX} \leq P_{CMAX} + T(P_{CMAX})$$

Where  $T(P_{CMAX})$  is defined by the tolerance table below and applies to  $P_{CMAX\_L}$  and  $P_{CMAX\_H}$  separately. If the  $P_{EMAX}$  is specially informed/declared that it would be settled as fixed level, the tolerance  $T(P_{CMAX})$  should be aligned with the corresponding requirement for rated output power for Relay backhaul link and the test could focus on the specific range.

If the informed/declared  $P_{EMAX}$  is equal to  $PRAT$ ,  $P_{CMAX}$  could be tested together with  $PRAT$ .

**Table 6.2.2.1-1:  $P_{CMAX}$  tolerance**

| $P_{CMAX}$ [dBm]                 | Tolerance $T(P_{CMAX})$ [dB] |
|----------------------------------|------------------------------|
| $PRAT-3 \leq P_{CMAX} \leq PRAT$ | 2.0                          |
| $PRAT-4 \leq P_{CMAX} < PRAT-3$  | 2.5                          |
| $PRAT-5 \leq P_{CMAX} < PRAT-4$  | 3.0                          |
| $PRAT-6 \leq P_{CMAX} < PRAT-5$  | 3.5                          |
| $PRAT-13 \leq P_{CMAX} < PRAT-6$ | 4.0                          |
| $-50 \leq P_{CMAX} < PRAT-13$    | 6.0                          |

## 6.3 Output power dynamics

### 6.3.1 Minimum output power

The minimum controlled output power of the RN is defined as the broadband transmit power of the RN, i.e. the power in the channel bandwidth for all transmit bandwidth configurations (resource blocks), when the power is set to a minimum value. The minimum output power is defined as the mean power in one sub-frame (1ms).

#### 6.3.1.1 Minimum requirement

For a Relay backhaul link with one antenna connector the minimum output power shall not exceed -50dBm.

For a Relay backhaul link with multiple transmit antenna connectors, the requirement is FFS

### 6.3.2 ON/OFF time mask and transmitter OFF power

For a backhaul link with one antenna connector the ON/OFF time mask is specified in subclause 6.3.4 of TS36.101 [2]. The requirements for PRACH specified in subclause 6.3.4 of TS36.101 [2] does not apply.

For a backhaul link with multiple antenna connectors the ON/OFF time mask is specified in subclause 6.3.4B of TS36.101 [2]. The requirements for PRACH specified in subclause 6.3.4B of TS36.101 [2] does not apply.

For backhaul link the transmitter OFF power shall not exceed the values specified in Table 6.3.2-1.

**Table 6.3.2-1: Transmitter OFF power**

|                       | Channel bandwidth / Transmitter OFF power / measurement bandwidth |         |         |         |          |        |
|-----------------------|-------------------------------------------------------------------|---------|---------|---------|----------|--------|
|                       | 1.4 MHz                                                           | 3.0 MHz | 5 MHz   | 10 MHz  | 15 MHz   | 20 MHz |
| Transmitter OFF power | -66 dBm                                                           |         |         |         |          |        |
| Measurement bandwidth | 1.08 MHz                                                          | 2.7 MHz | 4.5 MHz | 9.0 MHz | 13.5 MHz | 18 MHz |

For the access link the transient period requirements are specified in subclause 6.4.2 of TS36.104 [3]. The requirements only apply for TDD Relay.

For the access link the transmitter off power requirements are specified in subclause 6.4.1 of TS36.104 [3]. The requirements only apply for TDD Relay.

### 6.3.3 Power control

For the backhaul link the absolute power tolerance requirements are specified in subclause 6.3.5.1 of TS36.101[2]. The requirements specified for PRACH in subclause 6.3.5.1 of TS36.104[3] does not apply. Note 2 in table 6.2.2-1 in TS36.101[2] does not apply.

For the backhaul link the relative power tolerance requirements are specified in subclause 6.3.5.2 of TS36.101[2]. The requirements specified for PRACH in subclause 6.3.5.1 of TS36.104[3] does not apply. Note 2 in table 6.2.2-1 in TS36.101[2] does not apply.

For the backhaul link the aggregate power control tolerance requirements are specified in subclause 6.3.5.3 of TS36.101[2].

For a backhaul link with multiple antenna connectors the UL-MIMO power control requirements are specified in subclause 6.3.5B of TS36.101[2].

For the access link the RE Power control dynamic range requirements are specified in subclause 6.3.1 of TS36.104[3].

For the access link the total power dynamic range requirements are specified in subclause 6.3.2 of TS36.104[3].

## 6.4 Transmitted signal quality

### 6.4.1 Frequency error

Frequency error is the measure of the difference between the actual transmitting frequency of Relay and the assigned frequency.

#### 6.4.1.1 Minimum requirement

For the backhaul link the modulated carrier frequency of the Relay shall be accurate to within  $\pm 0.1$  PPM observed over a period of one time slot (0.5 ms) compared to the carrier frequency received from the Donor eNode B.

For the access link the modulated carrier frequency of Relay shall be accurate to within  $\pm 0.1$  PPM observed over a period of one subframe(1ms).

### 6.4.2 EVM

For the backhaul link the EVM; requirements are specified in subclause 6.5.2.1 of TS36.101[2].

For the access link the EVM requirements are specified in subclause 6.5.2 of TS36.104[3].

### 6.4.3 Time alignment error

For the access link the time alignment error requirements are specified in subclause 6.5.3 of TS36.104 [3].

For the backhaul link the time alignment error requirement is specified in subclause 6.8.1 of TS36.101 [2].

### 6.4.4 DL RS power

For the access link the DL RS power requirement is specified in subclause 6.5.4 of TS 36.104 [3].

## 6.5 Unwanted emissions

Unwanted emissions consist of out-of-band emissions and spurious emissions [4]. Out of band emissions are unwanted emissions immediately outside the channel bandwidth resulting from the modulation process and non-linearity in the transmitter but excluding spurious emissions. Spurious emissions are emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emission, intermodulation products and frequency conversion products, but exclude out of band emissions.

The out-of-band emissions requirement for the BS transmitter is specified in terms of an Operating band unwanted emissions requirement that defines limits for emissions in the downlink operating band plus the frequency ranges 10 MHz above and 10 MHz below the band. Emissions outside of this frequency range are limited by a spurious emissions requirement.

### 6.5.1 Transmitter spurious emissions

The spurious emission requirements are specified in subclause 6.6.4.1 of TS 36.104[3].

For a FDD Relay the requirements for protecting the own receiver are specified in subclause 6.6.4.2 of TS 36.104[3].

The requirements for protecting systems operating in other frequency bands are specified in subclause 6.6.4.3 of TS 36.104[3].

The requirements for protecting other co-located nodes are specified in table 6.6.4.4.1-2 of TS 36.104[3].

### 6.5.2 Adjacent Channel Leakage power Ratio (ACLR)

The ACLR requirements are specified in subclause 6.6.2.1 of TS 36.104[3].

### 6.5.3 Operating band unwanted emissions

Unless otherwise stated, the Operating band unwanted emission limits are defined from 10 MHz below the lowest frequency of the operating band up to 10 MHz above the highest frequency of the operating band.

The requirements shall apply whatever the type of transmitter considered (single carrier or multi-carrier) and for all transmission modes foreseen by the manufacturer's specification.

The unwanted emission limits in the part of the operating band that falls in the spurious domain are consistent with ITU-R Recommendation SM.329 [4].

#### 6.5.3.1 Minimum requirements

Emissions shall not exceed the maximum levels specified in the tables below, where:

- $\Delta f$  is the separation between the channel edge frequency and the nominal -3dB point of the measuring filter closest to the carrier frequency.
- $f\_offset$  is the separation between the channel edge frequency and the centre of the measuring filter.
- $f\_offset_{max}$  is the offset to the frequency 10 MHz outside the operating band.
- $\Delta f_{max}$  is equal to  $f\_offset_{max}$  minus half of the bandwidth of the measuring filter.

**Table 6.5.3.1-1: Relay operating band unwanted emission limits for 1.4 MHz channel bandwidth**

| Parameter                                                            | Value                                                                                            |                                                      |                                                     |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|
| Frequency offset of measurement filter -3dB point, $\Delta f$        | $0 \text{ MHz} \leq \Delta f < 1.4 \text{ MHz}$                                                  | $1.4 \text{ MHz} \leq \Delta f < 2.8 \text{ MHz}$    | $2.8 \text{ MHz} \leq \Delta f < \Delta f_{max}$    |
| Frequency offset of measurement filter centre frequency, $f\_offset$ | $0.05 \text{ MHz} \leq f\_offset < 1.45 \text{ MHz}$                                             | $1.45 \text{ MHz} \leq f\_offset < 2.85 \text{ MHz}$ | $2.85 \text{ MHz} \leq f\_offset < f\_offset_{max}$ |
| Measurement bandwidth (Note 1)                                       | 100 kHz                                                                                          | 100 kHz                                              | 100 kHz                                             |
| Minimum requirement Power class 1                                    | $-21 \text{ dBm} - \frac{10}{1.4} \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | -31 dBm                                              | -31 dBm                                             |
| Minimum requirement Power class 2                                    | $-15 \text{ dBm} - \frac{10}{1.4} \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | -25 dBm                                              | -25 dBm                                             |

**Table 6.5.3.1-2: Relay operating band unwanted emission limits for 3 MHz channel bandwidth**

| Parameter                                                            | Value                                                                                          |                                                      |                                                      |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|                                                                      | $0 \text{ MHz} \leq \Delta f < 3 \text{ MHz}$                                                  | $3 \text{ MHz} \leq \Delta f < 6 \text{ MHz}$        | $6 \text{ MHz} \leq \Delta f < \Delta f_{\max}$      |
| Frequency offset of measurement filter -3dB point, $\Delta f$        |                                                                                                |                                                      |                                                      |
| Frequency offset of measurement filter centre frequency, $f\_offset$ | $0.05 \text{ MHz} \leq f\_offset < 3.05 \text{ MHz}$                                           | $3.05 \text{ MHz} \leq f\_offset < 6.05 \text{ MHz}$ | $6.05 \text{ MHz} \leq f\_offset < f\_offset_{\max}$ |
| Measurement bandwidth (Note 1)                                       | 100 kHz                                                                                        | 100 kHz                                              | 100 kHz                                              |
| Minimum requirement Power class 1                                    | $-25 \text{ dBm} - \frac{10}{3} \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | -35 dBm                                              | -35 dBm                                              |
| Minimum requirement Power class 2                                    | $-25 \text{ dBm} - \frac{10}{3} \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | -29 dBm                                              | -29 dBm                                              |

**Table 6.5.3.1-3: Relay operating band unwanted emission limits for 5, 10, 15 and 20 MHz channel bandwidth**

| Parameter                                                            | Value                                                                                         |                                                                               |                                                       |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------|
|                                                                      | $0 \text{ MHz} \leq \Delta f < 5 \text{ MHz}$                                                 | $5 \text{ MHz} \leq \Delta f < \min(10 \text{ MHz}, \Delta f_{\max})$         | $10 \text{ MHz} \leq \Delta f < \Delta f_{\max}$      |
| Frequency offset of measurement filter -3dB point, $\Delta f$        |                                                                                               |                                                                               |                                                       |
| Frequency offset of measurement filter centre frequency, $f\_offset$ | $0.05 \text{ MHz} \leq f\_offset < 5.05 \text{ MHz}$                                          | $5.05 \text{ MHz} \leq f\_offset < \min(10.05 \text{ MHz}, f\_offset_{\max})$ | $10.05 \text{ MHz} \leq f\_offset < f\_offset_{\max}$ |
| Measurement bandwidth (Note 1)                                       | 100 kHz                                                                                       | 100 kHz                                                                       | 100 kHz                                               |
| Minimum requirement Power class 1                                    | $-30 \text{ dBm} - \frac{7}{5} \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | -37 dBm                                                                       | -37 dBm (Note 2)                                      |
| Minimum requirement Power class 2                                    | $-24 \text{ dBm} - \frac{7}{5} \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | -31 dBm                                                                       | -31 dBm                                               |

NOTE 1: As a general rule for the requirements in subclause 6.5.3, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE 2: The requirement is not applicable when  $\Delta f_{\max} < 10 \text{ MHz}$ .

## 6.6 Transmitter intermodulation

The transmitter requirements are specified in subclause 6.7 of TS 36.104[3].

# 7 Receiver characteristics

## 7.1 General

## 7.2 Reference sensitivity level

### 7.2.1 Backhaul link reference sensitivity

The reference sensitivity power level REFSENS is the minimum mean power applied to both the backhaul antenna ports at which the throughput shall meet or exceed the requirements for the specified reference measurement channel.

#### 7.2.1.1 Minimum requirement

The throughput shall be  $\geq 95\%$  of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 of TS 36.101[2] (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 of TS 36.101[2]) with parameters specified in Table 7.1.1.1-1.

NOTE: Whether the transmitter should be turned on or not during tests is FFS.

**Table 7.2.1.1-1: Backhaul antenna connector reference sensitivity**

| E-UTRA channel bandwidth [MHz] | Reference sensitivity power level, PREFSENS [dBm] |
|--------------------------------|---------------------------------------------------|
| 1.4                            | -105.7                                            |
| 3                              | -102.7                                            |
| 5                              | -101                                              |
| 10                             | -98                                               |
| 15                             | -96.2                                             |
| 20                             | -95                                               |

### 7.2.2 Access link reference sensitivity

The reference sensitivity power level PREFSENS is the minimum mean power received at the antenna connector at which a throughput requirement shall be met for a specified reference measurement channel.

#### 7.2.2.1 Minimum requirement

The throughput shall be  $\geq 95\%$  of the maximum throughput of the reference measurement channel as specified in Annex A of TS 36.104[3] with parameters specified in Table 7.2.2.1-1

**Table 7.2.2.1-1: Access link antenna connector reference sensitivity**

| E-UTRA channel bandwidth [MHz] | Reference measurement channel of Annex A.1 in TS 36.104 | Reference sensitivity power level, PREFSENS [dBm] |                     |
|--------------------------------|---------------------------------------------------------|---------------------------------------------------|---------------------|
|                                |                                                         | Relay power class 1                               | Relay Power class 2 |
| 1.4                            | FRC A1-1                                                | -98.8                                             | -98.8               |
| 3                              | FRC A1-2                                                | -95.0                                             | -95.0               |
| 5                              | FRC A1-3                                                | -93.5                                             | -93.5               |
| 10                             | FRC A1-3*                                               | -93.5                                             | -93.5               |
| 15                             | FRC A1-3*                                               | -93.5                                             | -93.5               |
| 20                             | FRC A1-3*                                               | -93.5                                             | -93.5               |

Note\*: PREFSENS is the power level of a single instance of the reference measurement channel. This requirement shall be met for each consecutive application of a single instance of FRC A1-3 mapped to disjoint frequency ranges with a width of 25 resource blocks each

## 7.3 Dynamic range

### 7.3.1 Backhaul link maximum input level

For the backhaul link the maximum input level requirements are specified in subclause 7.4 of TS 36.101[2]. For reference channels defined in Annex A.3.2 only measurement channels for UE category 3-5 should be used.

### 7.3.2 Access link Receiver Dynamic Range

For the access link the receiver dynamic range requirements are specified in subclause 7.3 of TS 36.104[3]. Only requirements in table 7.3.1-2 for local area shall apply.

## 7.4 In-channel selectivity

### 7.4.1 Access link in-channel selectivity

For the access link the in-channel selectivity requirements are specified in subclause 7.4 of TS 36.104[3]. Only requirements in table 7.4.1-2 for local area shall apply.

## 7.5 Adjacent Channel Selectivity (ACS)

Adjacent Channel Selectivity (ACS) is a measure of a receiver's ability to receive an E-UTRA signal at its assigned channel frequency in the presence of an adjacent channel signal at a given frequency offset from the centre frequency of the assigned channel. ACS is the ratio of the receive filter attenuation on the assigned channel frequency to the receive filter attenuation on the adjacent channel(s).

### 7.5.1 Backhaul link Adjacent Channel Selectivity

#### 7.5.1.1 Minimum requirement

The wanted and the interfering signal coupled to the backhaul antenna input are specified in Tables 7.5.1.1-1 and 7.5.1.1-2.

The throughput shall be  $\geq 95\%$  of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 of TS 36.101[2] (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 of TS 36.101[2]).

**Table 7.5.1.1-1: Adjacent Channel Selectivity for relay backhaul link (large wanted signal power)**

| E-UTRA channel bandwidth [MHz] | Wanted signal mean power [dBm]                                                         | Interfering signal mean power [dBm] | Interfering signal centre frequency offset from the channel edge of the wanted signal [MHz] | Type of interfering signal |
|--------------------------------|----------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------|----------------------------|
| 1.4                            | $P_{\text{REFSENS}} + 40.5\text{dB}^*$                                                 | -25                                 | 0.7025                                                                                      | 1.4MHz E-UTRA signal       |
| 3                              | $P_{\text{REFSENS}} + 35.5\text{dB}^*$                                                 | -25                                 | 1.5075                                                                                      | 3MHz E-UTRA signal         |
| 5                              | $P_{\text{REFSENS}} + 33.5\text{dB}^*$                                                 | -25                                 | 2.5025                                                                                      | 5MHz E-UTRA signal         |
| 10                             | $P_{\text{REFSENS}} + 33.5\text{dB}^*$                                                 | -25                                 | 2.5075                                                                                      | 5MHz E-UTRA signal         |
| 15                             | $P_{\text{REFSENS}} + 33.5\text{dB}^*$                                                 | -25                                 | 2.5125                                                                                      | 5MHz E-UTRA signal         |
| 20                             | $P_{\text{REFSENS}} + 33.5\text{dB}^*$                                                 | -25                                 | 2.5025                                                                                      | 5MHz E-UTRA signal         |
| Note*:                         | $P_{\text{REFSENS}}$ depends on the channel bandwidth as specified in Table 7.2.1.1-1. |                                     |                                                                                             |                            |

**Table 7.5.1.1-2: Adjacent Channel Selectivity for relay backhaul link (low wanted signal power)**

| E-UTRA channel bandwidth [MHz]                                                                | Wanted signal mean power [dBm] | Interfering signal mean power [dBm] | Interfering signal centre frequency offset from the channel edge of the wanted signal [MHz] | Type of interfering signal |
|-----------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------|----------------------------|
| 1.4                                                                                           | P <sub>REFSENS</sub> + 21 dB*  | -44.5                               | 0.7025                                                                                      | 1.4MHz E-UTRA signal       |
| 3                                                                                             | P <sub>REFSENS</sub> + 16 dB*  | -44.5                               | 1.5075                                                                                      | 3MHz E-UTRA signal         |
| 5                                                                                             | P <sub>REFSENS</sub> + 14 dB*  | -44.5                               | 2.5025                                                                                      | 5MHz E-UTRA signal         |
| 10                                                                                            | P <sub>REFSENS</sub> + 14 dB*  | -44.5                               | 2.5075                                                                                      | 5MHz E-UTRA signal         |
| 15                                                                                            | P <sub>REFSENS</sub> + 14 dB*  | -44.5                               | 2.5125                                                                                      | 5MHz E-UTRA signal         |
| 20                                                                                            | P <sub>REFSENS</sub> + 14 dB*  | -44.5                               | 2.5025                                                                                      | 5MHz E-UTRA signal         |
| Note*: P <sub>REFSENS</sub> depends on the channel bandwidth as specified in Table 7.2.1.1-1. |                                |                                     |                                                                                             |                            |

### 7.5.2 Access link Adjacent Channel Selectivity

For the access link the adjacent channel selectivity requirements are specified in subclause 7.5.1 of TS 36.104[3]. The Local Area BS requirements shall apply to the access link.

## 7.6 Blocking characteristics

### 7.6.1 Backhaul link blocking characteristics

#### 7.6.1.1 Minimum requirement

The wanted and the interfering signal coupled to the backhaul antenna input are specified in Tables 7.6.1.1-1 and 7.6.1.1-2.

The throughput shall be  $\geq 95\%$  of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 of TS 36.101[2] (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 of TS 36.101[2]).

**Table 7.6.1.1-1: Blocking performance requirement for backhaul link**

| Operating Band                             | Centre Frequency of Interfering Signal [MHz]                          | Interfering Signal mean power [dBm] | Wanted Signal mean power [dBm] | Interfering signal centre frequency minimum frequency offset from the channel edge of the wanted signal [MHz] | Type of Interfering Signal |
|--------------------------------------------|-----------------------------------------------------------------------|-------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------|
| 1-7, 9-11, 13-14, 18,19, 21, 23, 24, 33-43 | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +20)               | -15                                 | P <sub>REFSENS</sub> +33.5dB*  | See table 7.6.1.1-2                                                                                           | See table 7.6.1.1-2        |
|                                            | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +20) to 12750 | -15                                 | P <sub>REFSENS</sub> +6dB*     | -                                                                                                             | CW carrier                 |
| 8                                          | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +10)               | -15                                 | P <sub>REFSENS</sub> +33.5dB*  | See table 7.6.1.1-2                                                                                           | See table 7.6.1.1-2        |
|                                            | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +10) to 12750 | -15                                 | P <sub>REFSENS</sub> +6dB*     | -                                                                                                             | CW carrier                 |
| 12                                         | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +13)               | -15                                 | P <sub>REFSENS</sub> +33.5dB*  | See table 7.6.1.1-2                                                                                           | See table 7.6.1.1-2        |
|                                            | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +13) to 12750 | -15                                 | P <sub>REFSENS</sub> +6dB*     | -                                                                                                             | CW carrier                 |
| 17                                         | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +18)               | -15                                 | P <sub>REFSENS</sub> +33.5dB*  | See table 7.6.1.1-2                                                                                           | See table 7.6.1.1-2        |
|                                            | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +18) to 12750 | -15                                 | P <sub>REFSENS</sub> +6dB*     | -                                                                                                             | CW carrier                 |
| 20                                         | (F <sub>UL_low</sub> -11) to (F <sub>UL_high</sub> +20)               | -15                                 | P <sub>REFSENS</sub> +33.5dB*  | See table 7.6.1.1-2                                                                                           | See table 7.6.1.1-2        |
|                                            | 1 to (F <sub>UL_low</sub> -11)<br>(F <sub>UL_high</sub> +20) to 12750 | -15                                 | P <sub>REFSENS</sub> +6dB*     | -                                                                                                             | CW carrier                 |
| 25                                         | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +15)               | -15                                 | P <sub>REFSENS</sub> +33.5dB*  | See table 7.6.1.1-2                                                                                           | See table 7.6.1.1-2        |
|                                            | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +15) to 12750 | -15                                 | P <sub>REFSENS</sub> +6dB*     | -                                                                                                             | CW carrier                 |

Note\*: P<sub>REFSENS</sub> depends on the channel bandwidth as specified in Table 7.2.1.1-1.

**Table 7.6.1.1-2: Interfering signals for blocking performance requirement**

| E-UTRA channel BW of the lowest (highest) carrier received [MHz] | Interfering signal centre frequency minimum offset to the lower (higher) edge [MHz] | Type of interfering signal |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------|
| 1.4                                                              | ±2.1                                                                                | 1.4MHz E-UTRA signal       |
| 3                                                                | ±4.5                                                                                | 3MHz E-UTRA signal         |
| 5                                                                | ±7.5                                                                                | 5MHz E-UTRA signal         |
| 10                                                               | ±7.5                                                                                | 5MHz E-UTRA signal         |
| 15                                                               | ±7.5                                                                                | 5MHz E-UTRA signal         |
| 20                                                               | ±7.5                                                                                | 5MHz E-UTRA signal         |

### 7.6.2 Access link blocking characteristics

For the access link the blocking requirements are specified in subclause 7.6.1 of TS 36.104 [3]. The Local Area BS requirements shall apply for the access link.

### 7.6.3 Blocking requirements for co-location

For the backhaul link the blocking requirements for co-location are specified in subclause 7.6.2 of TS 36.104[3]. The Local Area BS requirements shall apply for the backhaul link.

For the access link the blocking requirements for co-location are specified in subclause 7.6.2 of TS 36.104[3]. The Local Area BS requirements shall apply for the access link for relay power class 1. For relay power class 2 the interfering signal power in table 7.6.2.1-2 of TS 36.104[3] shall be changed to 0 dBm.

## 7.7 Receiver spurious emissions

For the backhaul link the spurious emission requirements are specified in subclause 7.9 of TS 36.101[2].

For the access link the spurious emission requirements are specified in subclause 7.7 of TS 36.104[3].

## 7.8 Receiver intermodulation

### 7.8.1 Backhaul link receiver intermodulation

The receiver IM is a measure of the capability of the receiver to receive a wanted signal on its assigned channel frequency in the presence of two or more interfering signals which have a specific frequency relationship to the wanted signal.

#### 7.8.1.1 Minimum requirement

The wanted and the interfering signals coupled to the backhaul antenna input are specified in tables 7.8.1.1-1

The throughput shall be  $\geq 95\%$  of the maximum throughput of the reference measurement channels as specified in Annexes A.2.2, A.2.3 and A.3.2 of TS 36.101[2] (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1 of TS 36.101[2])

**Table 7.8.1.1-1: Wide band intermodulation for relay backhaul link**

| Rx Parameter                                  | Units                                                                                                                                                                                                                                                                                                                                                        | Channel bandwidth                                |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------------------|-------------------------------------|--------|--------|--------|--|--|--|--|--|--|--|--|--|--|
|                                               |                                                                                                                                                                                                                                                                                                                                                              | 1.4 MHz                                          | 3 MHz                               | 5 MHz                               | 10 MHz | 15 MHz | 20 MHz |  |  |  |  |  |  |  |  |  |  |
| Power in Transmission Bandwidth Configuration | dBm                                                                                                                                                                                                                                                                                                                                                          | REFSENS + channel bandwidth specific value below |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |
|                                               |                                                                                                                                                                                                                                                                                                                                                              | 12                                               | 8                                   | 6                                   | 6      | 6      | 6      |  |  |  |  |  |  |  |  |  |  |
| $P_{\text{Interferer 1}}$ (CW)                | dBm                                                                                                                                                                                                                                                                                                                                                          | -42                                              |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |
| $P_{\text{Interferer 2}}$ (Modulated)         | dBm                                                                                                                                                                                                                                                                                                                                                          | -42                                              |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |
| $BW_{\text{Interferer 2}}$                    |                                                                                                                                                                                                                                                                                                                                                              | 1.4                                              | 3                                   | 5                                   |        |        |        |  |  |  |  |  |  |  |  |  |  |
| $F_{\text{Interferer 1}}$ (Offset)            | MHz                                                                                                                                                                                                                                                                                                                                                          | $-BW/2 - 2.1$<br>/<br>$+BW/2 + 2.1$              | $-BW/2 - 2.1$<br>/<br>$+BW/2 + 2.1$ | $-BW/2 - 7.5$<br>/<br>$+BW/2 + 7.5$ |        |        |        |  |  |  |  |  |  |  |  |  |  |
| $F_{\text{Interferer 2}}$ (Offset)            | MHz                                                                                                                                                                                                                                                                                                                                                          | $2 \cdot F_{\text{Interferer 1}}$                |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |
| Note 1:                                       | Reference measurement channel is specified in TS36.101[2] Annex A.3.2 with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1.                                                                                                                                                                                                |                                                  |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |
| Note 2:                                       | The modulated interferer consists of the Reference measurement channel specified in TS36.101 Annex A.3.2 with one sided dynamic OCNG Pattern OP.1 FDD/TDD as described in Annex A.5.1.1/A.5.2.1 with set-up according to Annex C.3.1 The interfering modulated signal is 5MHz E-UTRA signal as described in Annex D for channel bandwidth $\geq 5\text{MHz}$ |                                                  |                                     |                                     |        |        |        |  |  |  |  |  |  |  |  |  |  |

### 7.8.2 Access link receiver intermodulation

For the access link the receiver intermodulation requirements are specified in subclause 7.8 of TS 36.104[3]. The Local Area BS requirements shall apply for the access link.

# 8 Access Performance requirement

## 8.1 General

Performance requirements for the access link are specified for the fixed reference channels defined in Annex A and the propagation conditions in Annex B of TS 36.104 [3]. The requirements only apply to those FRCs that are supported by the relay.

Unless stated otherwise, performance requirements apply for a single carrier only.

The SNR used in this clause is specified based on a single carrier and defined as:

$$\text{SNR} = S / N$$

Where:

S is the total signal energy in the subframe on a single antenna port.

N is the noise energy in a bandwidth corresponding to the transmission bandwidth over the duration of a subframe.

## 8.2 Performance requirements for PUSCH

### 8.2.1 Requirements in multipath fading propagation conditions

The PUSCH performance requirements in multipath fading propagation conditions are the same as defined in TS 36.104 [3]. The requirements associated with ETU 70Hz or ETU 300Hz are optional.

### 8.2.2 Requirements for UL timing adjustment

The requirements for UL timing adjustment are the same as defined in TS 36.104 [3].

### 8.2.3 Requirements for HARQ-ACK multiplexed on PUSCH

The performance requirements for HARQ-ACK multiplexed on PUSCH are the same as defined in TS 36.104 [3]. The requirements associated with ETU 70Hz are optional.

## 8.3 Performance requirements for PUCCH

### 8.3.1 DTX to ACK performance

The DTX to ACK performance requirements are the same as defined in TS 36.104 [3].

### 8.3.2 ACK missed detection requirements for single user PUCCH format 1a

The ACK missed detection requirements for single user PUCCH format 1a are the same as defined in TS 36.104 [3]. The requirements associated with ETU 70Hz or ETU 300Hz are optional.

### 8.3.3 CQI missed detection requirements for PUCCH format 2

The CQI missed detection requirements for PUCCH format 2 are the same as defined in TS 36.104 [3]. The requirements associated with ETU 70Hz are optional.

### 8.3.4 ACK missed detection requirements for multi user PUCCH format 1a

The ACK missed detection requirements for multi user PUCCH format 1a are optional and are the same as defined in TS 36.104 [3].

## 8.4 Performance requirements for PRACH

### 8.4.1 PRACH False alarm probability

The requirements for PRACH False alarm probability are the same as defined in TS 36.104 [3].

### 8.4.2 PRACH detection requirements

The PRACH detection requirements are the same as defined in TS 36.104 [3]. The requirements associated with ETU 70Hz are optional.

# 9 Backhaul Performance requirement

## 9.1 General

The performance requirements for the backhaul are based on relays that utilize a dual-antenna receiver.

For all test cases, the SNR is defined as:

$$\text{SNR} = \frac{\hat{E}_s^{(1)} + \hat{E}_s^{(2)}}{N_{oc}^{(1)} + N_{oc}^{(2)}}$$

where the superscript indicates the receiver antenna connector. The above SNR definition assumes that the REs are not precoded. The SNR definition does not account for any gain which can be associated to the precoding operation. The relative power of physical channels transmitted is defined in TS 36.101[2] Table C.3.2-1. The symbols of  $\hat{E}_s$  and  $N_{oc}$  are defined in TS36.101 [2].

## 9.2 Demodulation of PDSCH (Cell-Specific Reference Symbols)

The requirements for demodulation of PDSCH with Cell-Specific Reference Symbols are defined in TS 36.101[2] subclause 8.2. The requirements associated with ETU 300Hz or high speed train propagation condition are optional.

## 9.3 Demodulation of PDSCH (User-Specific Reference Symbols)

The requirements for demodulation of PDSCH with User-Specific Reference Symbols are defined in TS 36.101[2] subclause 8.3.

## 9.4 Demodulation of PDCCH/PCFICH

The requirements for demodulation of PDCCH/PCFICH are defined in TS 36.101[2] subclause 8.4.

## 9.5 Demodulation of PHICH

The requirements for demodulation of PHICH are defined in TS 36.101[2] subclause 8.5.

## 9.6 Demodulation of PBCH

The requirements for demodulation of PBCH are defined in TS 36.101[2] subclause 8.6.

## 9.7 Sustained downlink data rate provided by lower layers

The requirements for sustained downlink data rate provided by lower layers are defined in TS 36.101[2] subclause 8.7.

## 9.8 Demodulation of R-PDCCH

The requirements are valid for the propagation conditions given in Annex A and for the reference channels provided in Annex B.

### 9.8.1 R-PDCCH format without cross-interleaving

#### 9.8.1.1 FDD

For single-layer transmission on antenna port 7, the requirements are specified in Table 9.8.1.1-2, with parameters in Table 9.8.1.1-1.

**Table 9.8.1.1-1: Test Parameters for single-layer transmission on port 7 of R-PDCCH**

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Unit                  | Test 1                                       | Test 2                                                                                                                                                          |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Cyclic prefix                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                       | Normal                                       |                                                                                                                                                                 |  |
| Cell ID                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                       | 0                                            |                                                                                                                                                                 |  |
| Un subframe type in DeNB                                                                                                                                                                                                                                                                                                                                                                                                                                        |                       | Normal subframe                              |                                                                                                                                                                 |  |
| SubframeConfigurationFDD                                                                                                                                                                                                                                                                                                                                                                                                                                        |                       | 10110101                                     |                                                                                                                                                                 |  |
| Number of OFDM symbols for PDCCH                                                                                                                                                                                                                                                                                                                                                                                                                                | OFDM symbols          | 2                                            |                                                                                                                                                                 |  |
| Configuration of OFDM symbols for eNB-to-RN transmission in the first slot                                                                                                                                                                                                                                                                                                                                                                                      |                       | 2 (Note 1)                                   |                                                                                                                                                                 |  |
| Downlink power allocation                                                                                                                                                                                                                                                                                                                                                                                                                                       | R-PDCCH_RA<br>OCNG_RA | dB                                           | 0                                                                                                                                                               |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | R-PDCCH_RB<br>OCNG_RB | dB                                           | 0                                                                                                                                                               |  |
| Cell-specific reference symbols                                                                                                                                                                                                                                                                                                                                                                                                                                 |                       | Antenna port 0                               | Antenna port 0,1                                                                                                                                                |  |
| CSI reference signal configuration                                                                                                                                                                                                                                                                                                                                                                                                                              |                       | 1                                            |                                                                                                                                                                 |  |
| Number of CSI reference signals configured                                                                                                                                                                                                                                                                                                                                                                                                                      |                       | 1                                            | 4                                                                                                                                                               |  |
| CSI reference signal subframe configuration                                                                                                                                                                                                                                                                                                                                                                                                                     |                       | $I_{CSI-RS} = 37$                            |                                                                                                                                                                 |  |
| $N_{oc}$ at antenna port                                                                                                                                                                                                                                                                                                                                                                                                                                        | dBm/15kHz             | -98                                          |                                                                                                                                                                 |  |
| Number of allocated resource blocks                                                                                                                                                                                                                                                                                                                                                                                                                             | PRB                   | 2                                            | 4                                                                                                                                                               |  |
| Unused REs and PRBs                                                                                                                                                                                                                                                                                                                                                                                                                                             |                       | OCNG (Note 2)                                |                                                                                                                                                                 |  |
| Simultaneous transmission (Note 3)                                                                                                                                                                                                                                                                                                                                                                                                                              |                       | No                                           |                                                                                                                                                                 |  |
| Beamforming Model                                                                                                                                                                                                                                                                                                                                                                                                                                               |                       | No precoding                                 | a precoder vector $W(i)$ of size $4 \times 1$ is randomly selected with the number of layers $v = 1$ from Table 6.3.4.2.3-2 in TS 36.211 as beamforming weights |  |
| Precoder update granularity                                                                                                                                                                                                                                                                                                                                                                                                                                     |                       | Frequency domain: 1 PRG<br>Time domain: 1 ms |                                                                                                                                                                 |  |
| Note 1: as specified in Table 5.4-1 in TS 36.216<br>Note 2: These physical resource blocks are assigned to an arbitrary number of virtual UEs with one PDSCH per virtual UE; the data transmitted over the OCNG PDSCHs or other OCGN REs shall be uncorrelated pseudo random data, which is QPSK modulated.<br>Note 3: The modulation symbols of the signal under test are mapped onto antenna port 7 while antenna port 8 is unused.<br>Note 4: $n_{SCID} = 0$ |                       |                                              |                                                                                                                                                                 |  |

**Table 9.8.1.1-2: Minimum performance for R-PDCCH without cross-interleaving (FRC)**

| Test number | Bandwidth | Reference channel | OCNG Pattern | Aggregation level | DCI format | Propagation Condition              | Antenna configuration and correlation Matrix | Reference value |          |
|-------------|-----------|-------------------|--------------|-------------------|------------|------------------------------------|----------------------------------------------|-----------------|----------|
|             |           |                   |              |                   |            |                                    |                                              | Pm-dsg (%)      | SNR (dB) |
| 1           | 10MHz     | R.1 FDD           | OP.1 FDD     | 2 PRB             | Format 2C  | LOS with strong dominant component | 1x2                                          | 1               | 2.1      |
| 2           | 10 MHz    | R.2 FDD           | OP.1 FDD     | 4 PRB             | Format 2C  | NLOS with medium correlation       | 4x2                                          | 1               | 11.5     |

#### 9.8.1.2 TDD

For single-layer transmission on antenna port 7, the requirements are specified in Table 9.8.1.2-2, with parameters in Table 9.8.1.2-1.

**Table 9.8.1.2-1: Test Parameters for single-layer transmission on port 7 of R-PDCCH**

| Parameter                                                                  | Unit                                                                                                                                                                                                                                            | Test 1                                       | Test 2                                                                                                                                                          |  |  |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Cyclic prefix                                                              |                                                                                                                                                                                                                                                 | Normal                                       |                                                                                                                                                                 |  |  |
| Cell ID                                                                    |                                                                                                                                                                                                                                                 | 0                                            |                                                                                                                                                                 |  |  |
| Un subframe type in DeNB                                                   |                                                                                                                                                                                                                                                 | Normal subframe                              |                                                                                                                                                                 |  |  |
| Uplink downlink configuration                                              |                                                                                                                                                                                                                                                 | 1                                            |                                                                                                                                                                 |  |  |
| SubframeConfigurationTDD                                                   |                                                                                                                                                                                                                                                 | 4                                            |                                                                                                                                                                 |  |  |
| Number of OFDM symbols for PDCCH                                           | OFDM symbols                                                                                                                                                                                                                                    | 2                                            |                                                                                                                                                                 |  |  |
| Configuration of OFDM symbols for eNB-to-RN transmission in the first slot |                                                                                                                                                                                                                                                 | 2 (Note 1)                                   |                                                                                                                                                                 |  |  |
| Downlink power allocation                                                  | R-PDCCH_RA<br>OCNG_RA                                                                                                                                                                                                                           | dB                                           | 0                                                                                                                                                               |  |  |
|                                                                            | R-PDCCH_RB<br>OCNG_RB                                                                                                                                                                                                                           | dB                                           | 0                                                                                                                                                               |  |  |
| Cell-specific reference symbols                                            |                                                                                                                                                                                                                                                 | Antenna port 0                               | Antenna port 0,1                                                                                                                                                |  |  |
| CSI reference signal configuration                                         |                                                                                                                                                                                                                                                 | 1                                            |                                                                                                                                                                 |  |  |
| Number of CSI reference signals configured                                 |                                                                                                                                                                                                                                                 | 1                                            | 4                                                                                                                                                               |  |  |
| CSI reference signal subframe configuration                                |                                                                                                                                                                                                                                                 | $l_{CSI-RS} = 35$                            |                                                                                                                                                                 |  |  |
| $N_{oc}$ at antenna port                                                   | dBm/15kHz                                                                                                                                                                                                                                       | -98                                          |                                                                                                                                                                 |  |  |
| Number of allocated resource blocks                                        | PRB                                                                                                                                                                                                                                             | 2                                            | 4                                                                                                                                                               |  |  |
| Unused REs and PRBs                                                        |                                                                                                                                                                                                                                                 | OCNG (Note 2)                                |                                                                                                                                                                 |  |  |
| Simultaneous transmission (Note 3)                                         |                                                                                                                                                                                                                                                 | No                                           |                                                                                                                                                                 |  |  |
| Beamforming Model                                                          |                                                                                                                                                                                                                                                 | No precoding                                 | a precoder vector $W(i)$ of size $4 \times 1$ is randomly selected with the number of layers $v = 1$ from Table 6.3.4.2.3-2 in TS 36.211 as beamforming weights |  |  |
| Precoder update granularity                                                |                                                                                                                                                                                                                                                 | Frequency domain: 1 PRG<br>Time domain: 1 ms |                                                                                                                                                                 |  |  |
| Note 1:                                                                    | as specified in Table 5.4-1 in TS 36.216                                                                                                                                                                                                        |                                              |                                                                                                                                                                 |  |  |
| Note 2:                                                                    | These physical resource blocks are assigned to an arbitrary number of virtual UEs with one PDSCH per virtual UE; the data transmitted over the OCNG PDSCHs or other OCNG REs shall be uncorrelated pseudo random data, which is QPSK modulated. |                                              |                                                                                                                                                                 |  |  |
| Note 3:                                                                    | The modulation symbols of the signal under test are mapped onto antenna port 7 while antenna port 8 is unused.                                                                                                                                  |                                              |                                                                                                                                                                 |  |  |
| Note 4:                                                                    | $n_{scid} = 0$                                                                                                                                                                                                                                  |                                              |                                                                                                                                                                 |  |  |

**Table 9.8.1.2-2: Minimum performance for R-PDCCH without cross-interleaving (FRC)**

| Test number | Bandwidth | Reference channel | OCNG Pattern | Aggregation level | DCI format | Propagation Condition              | Antenna configuration and correlation Matrix | Reference value |          |
|-------------|-----------|-------------------|--------------|-------------------|------------|------------------------------------|----------------------------------------------|-----------------|----------|
|             |           |                   |              |                   |            |                                    |                                              | Pm-dsg (%)      | SNR (dB) |
| 1           | 10MHz     | R.1 TDD           | OP.1 TDD     | 2 PRB             | Format 2C  | LOS with strong dominant component | 1x2                                          | 1               | 2.1      |
| 2           | 10 MHz    | R.2 TDD           | OP.1 TDD     | 4 PRB             | Format 2C  | NLOS with medium correlation       | 4x2                                          | 1               | 11.5     |

# Annex A: Propagation models for relay demodulation requirements

## A.1 Propagation models for backhaul link

### A.1.1 Delay Profiles

Three representative delay profiles are selected corresponding to the LOS and NLOS scenarios.

#### A.1.1.1 LOS between eNB and relay

Table A.1.1-1 and Table A.1.1-2 show the delay profiles for the LOS scenarios: one with strong dominant component and the other with medium dominant component. Note that the first tap in both Table A.1.1-1 and Table A.1.1-2 corresponds to the LOS component, it is therefore a non-fading tap and the corresponding Doppler frequency is 0.

**Table A.1.1-1: Delay Profile for LOS Scenario (strong dominant component)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | 0.0                 |
| 30                    | -21.0               |
| 70                    | -22.0               |
| 90                    | -23.0               |

Note that as the first tap is at least 21dB stronger than the rest taps, this channel may be considered as an AWGN channel. The exact one-tap static AWGN channel model is FFS.

**Table A.1.1-2: Delay Profile for LOS Scenario (medium dominant component)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | 0.0                 |
| 30                    | -11.0               |
| 70                    | -12.0               |
| 90                    | -13.0               |
| 110                   | -18.0               |
| 190                   | -27.2               |
| 410                   | -30.8               |

Note that as the first tap is at least 11dB stronger than the rest taps, this channel may be characterized by one dominant path combined with significant scattering paths.

#### A.1.1.2 NLOS between eNB and relay

For NLOS scenario, the delay profile is given in Table A.1.1-3.

**Table A.1.1-3: Delay Profile for NLOS Scenario**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | 0.0                 |
| 30                    | -1.0                |
| 70                    | -2.0                |
| 90                    | -3.0                |
| 110                   | -8.0                |
| 190                   | -17.2               |
| 410                   | -20.8               |

### A.1.2 Doppler Frequency

For NLOS between the eNB and the relay, as the relay nodes are often fixed, hence a low Doppler frequency of 2Hz is used. Note that this 2Hz Doppler frequency is only used for the new channels (such as R-PDCCH).

### A.1.3 MIMO Correlation Matrices

For LOS component between the eNB and the relay, the spatial channel correlation matrix is modeled as an all one matrix unless cross-polarized antennas are deployed. This is because the correlation matrix for the channel with single LOS component is of rank 1.

For NLOS scenario, the correlation matrices are given in the following tables.

Table A.1.3-1 defines the correlation matrices for the eNB:

**Table A.1.3-1: eNB correlation matrix**

|                 | One antenna   | Two antennas                                                         | Four antennas                                                                                                                                                                                                                             |
|-----------------|---------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eNB Correlation | $R_{eNB} = 1$ | $R_{eNB} = \begin{pmatrix} 1 & \alpha \\ \alpha^* & 1 \end{pmatrix}$ | $R_{eNB} = \begin{pmatrix} 1 & \alpha^{1/9} & \alpha^{4/9} & \alpha \\ \alpha^{1/9*} & 1 & \alpha^{1/9} & \alpha^{4/9} \\ \alpha^{4/9*} & \alpha^{1/9*} & 1 & \alpha^{1/9} \\ \alpha^* & \alpha^{4/9*} & \alpha^{1/9*} & 1 \end{pmatrix}$ |

Table A.1.3-2 defines the correlation matrices for the relay:

**Table A.1.3-2: Relay correlation matrix**

|                   | One antenna     | Two antennas                                                         | Four antennas                                                                                                                                                                                                         |
|-------------------|-----------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Relay Correlation | $R_{Relay} = 1$ | $R_{Relay} = \begin{pmatrix} 1 & \beta \\ \beta^* & 1 \end{pmatrix}$ | $R_{Relay} = \begin{pmatrix} 1 & \beta^{19} & \beta^{49} & \beta \\ \beta^{19*} & 1 & \beta^{19} & \beta^{49} \\ \beta^{49*} & \beta^{19*} & 1 & \beta^{19} \\ \beta^* & \beta^{49*} & \beta^{19*} & 1 \end{pmatrix}$ |

The values of  $\alpha$  and  $\beta$  for different correlation types are given in Table A.1.3-3

**Table A.1.3-3: Low, Medium and High Correlation Values**

| Low correlation |         | Medium Correlation |         | High Correlation |         |
|-----------------|---------|--------------------|---------|------------------|---------|
| $\alpha$        | $\beta$ | $\alpha$           | $\beta$ | $\alpha$         | $\beta$ |
| 0               | 0       | 0.3                | 0.9     | 0.9              | 0.9     |

For the channel from the eNB to the relay, the channel spatial correlation matrix  $R_{spat}$  is then given as the Kronecker product of the eNB correlation matrix and the relay correlation matrix, i.e.  $R_{spat} = R_{eNB} \otimes R_{Relay}$ .

## A.2 Multipath propagation fading conditions for access link

Tables A.2-1 – Table A.2-3 show multi-path delay profiles that are used for the performance measurements in multi-path fading environment. All taps have classical Doppler spectrum, defined as:

$$(CLASS) \quad S(f) \propto 1/(1 - (f/f_D)^2)^{0.5} \quad \text{for } f \in -f_D, f_D$$

**Table A.2-1: Extended Pedestrian A model (EPA)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | 0.0                 |
| 30                    | -1.0                |
| 70                    | -2.0                |
| 90                    | -3.0                |
| 110                   | -8.0                |
| 190                   | -17.2               |
| 410                   | -20.8               |

**Table A.2-2: Extended Vehicular A model (EVA)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | 0.0                 |
| 30                    | -1.5                |
| 150                   | -1.4                |
| 310                   | -3.6                |
| 370                   | -0.6                |
| 710                   | -9.1                |
| 1090                  | -7.0                |
| 1730                  | -12.0               |
| 2510                  | -16.9               |

**Table A.2-3: Extended Typical Urban model (ETU)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | -1.0                |
| 50                    | -1.0                |
| 120                   | -1.0                |
| 200                   | 0.0                 |
| 230                   | 0.0                 |
| 500                   | 0.0                 |
| 1600                  | -3.0                |
| 2300                  | -5.0                |
| 5000                  | -7.0                |

A multipath fading propagation condition is defined by a combination of a multi-path delay profile and a maximum Doppler frequency  $f_D$  which is either 5, 70 or 300 Hz.

Note that the ETU model shown in Table A.2-3 and Doppler frequency of 300Hz are optional for relay access link demodulation requirements.

The relay access link demodulation requirements are the same or subset of the eNB requirements as described in TS 36.104.

# Annex B: Reference Measurement Channel

## B.1 Reference measurement channels for R-PDCCH performance requirements

### B.1.1 R-PDCCH format without cross-interleaving

#### B.1.1.1 FDD

**Table B.1.1.1-1: Fixed Reference Channel for R-PDCCH transmitted on single-layer antenna port 7**

| Parameter                      | Unit | Value     |                |
|--------------------------------|------|-----------|----------------|
|                                |      | R.1 FDD   | R.2 FDD        |
| Reference channel              |      |           |                |
| Number of transmitter antennas |      | 1         | 4              |
| Channel bandwidth              | MHz  | 10        | 10             |
| Allocated RB for R-PDCCH       | RB   | 24, 25    | 23, 24, 25, 26 |
| Aggregation level              | PRB  | 2         | 4              |
| DCI Format                     |      | Format 2C | Format 2C      |
| Cell ID                        |      | 0         | 0              |
| Payload (without CRC)          | Bits | 42        | 42             |

#### B.1.1.2 TDD

**Table B.1.1.2-1: Fixed Reference Channel for R-PDCCH transmitted on single-layer antenna port 7**

| Parameter                      | Unit | Value     |                |
|--------------------------------|------|-----------|----------------|
|                                |      | R.1 TDD   | R.2 TDD        |
| Reference channel              |      |           |                |
| Number of transmitter antennas |      | 1         | 4              |
| Channel bandwidth              | MHz  | 10        | 10             |
| Allocated RB for R-PDCCH       | RB   | 24, 25    | 23, 24, 25, 26 |
| Aggregation level              | PRB  | 2         | 4              |
| DCI Format                     |      | Format 2C | Format 2C      |
| Cell ID                        |      | 0         | 0              |
| Payload (without CRC)          | Bits | 45        | 45             |

## B.2 OCNG patterns for R-PDCCH performance requirements

The following OCNG patterns are used for modelling allocations to virtual UEs (which are not under test) and/or allocations used for MBSFN. The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG\_RA and OCNG\_RB which together with a relative power level ( $\gamma$ ) specifies the PDSCH EPRE-to-RS EPRE ratios in OFDM symbols with and without reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

$$\gamma_i = \text{PDSCH\_OCNG\_RA} / \text{PDSCH\_OCNG\_RB}$$

where  $\gamma_i$  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG\_RA, OCNG\_RB, and the set of relative power levels  $\gamma$  are chosen such that when also taking allocations to the UE under test into account, as

given by a PDSCH reference channel, a constant transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

Moreover the OCNG pattern is accompanied by a PCFICH/PDCCH/PHICH reference channel which specifies the control region. For any aggregation and PHICH allocation, the PDCCH and any unused PHICH groups are padded with resource element groups with a power level given respectively by PDCCH\_RA/RB and PHICH\_RA/RB as specified in the test case such that a total power spectral density in the control region that is constant on an OFDM symbol basis is targeted.

### B.2.1 FDD

#### B.2.1.1 OCNG FDD pattern 1for R-PDCCH

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is discontinuous (divided in two parts by the allocated area – two sided) or continuous (one sided) in the frequency domain, starts with PRB 0 and ends with PRB  $N_{RB}-1$ .

**Table B.2.1-1: OCNG for FDD R-PDCCH**

| Relative power level $\gamma_{PRB}$ [dB]                                |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                              |                                              |                                              | PDSCH Data |  |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|------------|--|
| Subframe                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                              |                                              |                                              |            |  |
| Allocated subframes for R-PDCCH                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                             | Subframes unallocated for R-PDCCH            |                                              |                                              |            |  |
| The 1 <sup>st</sup> slot                                                | The 2 <sup>nd</sup> slot                                                                                                                                                                                                                                                                                                                                                                                                                    | 0                                            | 5                                            | Other subframes                              |            |  |
| Allocation                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                              |                                              |                                              |            |  |
| 0 – (First allocated PRB-1) and (Last allocated PRB+1) – ( $N_{RB}-1$ ) | First unallocated PRB – Last unallocated PRB                                                                                                                                                                                                                                                                                                                                                                                                | First unallocated PRB – Last unallocated PRB | First unallocated PRB – Last unallocated PRB | First unallocated PRB – Last unallocated PRB |            |  |
| 0                                                                       | 0                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0                                            | 0                                            | 0                                            | Note 1     |  |
| Note 1:                                                                 | These physical resource blocks are assigned to an arbitrary number of virtual UEs with one PDSCH per virtual UE; the data transmitted over the OCNG PDSCHs shall be uncorrelated pseudo random data, which is QPSK modulated. The parameter $\gamma_{PRB}$ is used to scale the power of PDSCH.                                                                                                                                             |                                              |                                              |                                              |            |  |
| Note 2:                                                                 | If two or more transmit antennas with CRS are used in the test, the OCNG shall be transmitted to the virtual users by all the transmit antennas with CRS according to transmission mode 2. The parameter $\gamma_{PRB}$ applies to each antenna port separately, so the transmit power is equal between all the transmit antennas with CRS used in the test. The antenna transmission modes are specified in section 7.1 in 3GPP TS 36.213. |                                              |                                              |                                              |            |  |

### B.2.2 TDD

#### B.2.2.1 OCNG TDD pattern 1for R-PDCCH

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the subframes available for DL transmission (depending on TDD UL/DL configuration), when the unallocated area is discontinuous (divided in two parts by the allocated area – two sided) or continuous (one sided) in the frequency domain, starts with PRB 0 and ends with PRB  $N_{RB}-1$ .

Table B.2.2-1: OCNG for TDD R-PDCCH

| Relative power level $\gamma_{PRB}$ [dB]                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                    |                                                    |                                                    |                                                    | PDSCH Data |  |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|------------|--|
| Subframe (only if available for DL <sup>Note 2</sup> )                        |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                    |                                                    |                                                    |                                                    |            |  |
| Allocated subframes for R-PDCCH                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                             | Subframes unallocated for R-PDCCH                  |                                                    |                                                    |                                                    |            |  |
| The 1 <sup>st</sup> slot                                                      | The 2 <sup>nd</sup> slot                                                                                                                                                                                                                                                                                                                                                                                                                    | 0                                                  | 5                                                  | 1 and 6 (as special subframes)                     | Other normal subframes                             |            |  |
| Allocation                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                    |                                                    |                                                    |                                                    |            |  |
| 0 – (First allocated PRB-1)<br>and<br>(Last allocated PRB+1) – ( $N_{RB}$ -1) | First unallocated PRB<br>–<br>Last unallocated PRB                                                                                                                                                                                                                                                                                                                                                                                          | First unallocated PRB<br>–<br>Last unallocated PRB | First unallocated PRB<br>–<br>Last unallocated PRB | First unallocated PRB<br>–<br>Last unallocated PRB | First unallocated PRB<br>–<br>Last unallocated PRB |            |  |
| 0                                                                             | 0                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0                                                  | 0                                                  | 0                                                  | 0                                                  | Note 1     |  |
| Note 1:                                                                       | These physical resource blocks are assigned to an arbitrary number of virtual UEs with one PDSCH per virtual UE; the data transmitted over the OCNG PDSCHs shall be uncorrelated pseudo random data, which is QPSK modulated. The parameter $\gamma_{PRB}$ is used to scale the power of PDSCH.                                                                                                                                             |                                                    |                                                    |                                                    |                                                    |            |  |
| Note 2:                                                                       | Subframes available for DL transmission depends on the Uplink-Downlink configuration in Table 4.2-2 in 3GPP TS 36.211                                                                                                                                                                                                                                                                                                                       |                                                    |                                                    |                                                    |                                                    |            |  |
| Note 3:                                                                       | If two or more transmit antennas with CRS are used in the test, the OCNG shall be transmitted to the virtual users by all the transmit antennas with CRS according to transmission mode 2. The parameter $\gamma_{PRB}$ applies to each antenna port separately, so the transmit power is equal between all the transmit antennas with CRS used in the test. The antenna transmission modes are specified in section 7.1 in 3GPP TS 36.213. |                                                    |                                                    |                                                    |                                                    |            |  |

# Annex C: Change history

| Change history |            |           |      |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |        |        |
|----------------|------------|-----------|------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|
| Date           | TSG #      | TSG Doc.  | CR   | Rev | Subject/Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Old    | New    |
| 2010-10        | RAN<br>WG4 | R4-103714 |      |     | First Version                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | -      | 0.0.1  |
| 2010-11        | RAN4-57    | R4-104867 |      |     | The following TP are implemented:<br>R4-104383, "Abbreviations for Relay Core specification"<br>Editorial changes:<br>Version number, date and change history updated.                                                                                                                                                                                                                                                                                                               | 0.0.1  | 0.1.0  |
| 2011-02        | RAN4-58    | R4-111615 |      |     | The following TP are implemented:<br>R4-111174, "Abbreviations for Relay specification"<br>Editorial changes:<br>Specification number changed to TS 36.116<br>Version number, date and change history updated.                                                                                                                                                                                                                                                                       | 0.1.0  | 0.2.0  |
| 2012-08        | RAN4-64    | R4-124585 |      |     | The following TP are implemented:<br>R4-123515 "TP for 36.116 Relay core requirements"<br>Editorial changes:<br>Specification number changed to TS 36.116<br>Version number, date and change history updated.                                                                                                                                                                                                                                                                        | 0.2.0  | 0.3.0  |
| 2012-08        | RAN4-64    | R4-124918 |      |     | The following TP are implemented:<br>R4-124583, "TP for Relay TS: Generic chapter"<br>R4-124584, "TP for Relay TS: Performance requirements"<br>R4-124847, " TP for 36.116 on Relay Access Link DL RS power"<br>R4-124909, "Text Proposal for TS36.116 Subclause 6.4.3 Time alignment between transmitter branches"<br><br>Editorial changes:<br>Table of contents updated<br>Version number, date and change history updated.<br>Minor editorial fixes, e.g. inserting missing tabs | 0.3.0  | 0.4.0  |
| 2012-09        | RAN-57     | RP-121233 |      |     | Version for approval<br>Version number updated<br>Guidance text removed                                                                                                                                                                                                                                                                                                                                                                                                              | 0.4.0  | 1.0.0  |
| 2012-09        | RAN-57     |           |      |     | TR Approved by RAN-57                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 1.0.0  | 11.0.0 |
| 2012-12        | RAN-58     | RP-121904 | 0002 |     | Correction of relay demodulation requirements                                                                                                                                                                                                                                                                                                                                                                                                                                        | 11.0.0 | 11.1.0 |
| 2012-12        | RAN-58     | RP-121904 | 0003 |     | Corrections on Relay backhaul link R-PDCCH performance                                                                                                                                                                                                                                                                                                                                                                                                                               | 11.0.0 | 11.1.0 |
| 2013-03        | RP-59      | RP-130286 | 0001 | 1   | Correction of R-PDCCH test                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 11.1.0 | 11.2.0 |
| 2013-06        | RP-60      | RP-130770 | 0005 |     | Correction of Relay transmitter and receiver requirement                                                                                                                                                                                                                                                                                                                                                                                                                             | 11.2.0 | 11.3.0 |
| 2013-06        | RP-60      | RP-130770 | 0006 |     | Correction for Co-location blocking requirement in TS36.116<br>Section 7.6.3                                                                                                                                                                                                                                                                                                                                                                                                         | 11.2.0 | 11.3.0 |
| 2015-03        | RP-67      | RP-150384 | 0010 |     | Corrections for TS 36.116 clause 7.6: Blocking characteristics                                                                                                                                                                                                                                                                                                                                                                                                                       | 11.3.0 | 11.4.0 |
| 2015-07        | RP-68      | RP-150955 | 012  | 1   | Corrections on power class for relay backhaul link                                                                                                                                                                                                                                                                                                                                                                                                                                   | 11.4.0 | 11.5.0 |
| 2015-07        | RP-68      | RP-150955 | 014  | 1   | Clarification on requirement description for TS 36.116                                                                                                                                                                                                                                                                                                                                                                                                                               | 11.4.0 | 11.5.0 |
| 2015-09        | RP-69      | RP-151476 | 0016 | 1   | Correction on the transmitter requirements in TS36.116                                                                                                                                                                                                                                                                                                                                                                                                                               | 11.5.0 | 11.6.0 |
| 2015-12        | RP-70      | RP-152132 | 0018 |     | Removal of square brackets in TS 36.116Removal of square brackets in TS 36.116                                                                                                                                                                                                                                                                                                                                                                                                       | 11.6.0 | 11.7.0 |