





# Contents

|                                                                           |    |
|---------------------------------------------------------------------------|----|
| Foreword .....                                                            | 5  |
| 1 Scope.....                                                              | 6  |
| 2 References.....                                                         | 6  |
| 3 Definitions, symbols and abbreviations .....                            | 6  |
| 3.1 Definitions.....                                                      | 6  |
| 3.2 Symbols.....                                                          | 7  |
| 3.3 Abbreviations .....                                                   | 8  |
| 4 General.....                                                            | 8  |
| 4.1 Relationship between Minimum Requirements and Test Requirements ..... | 8  |
| 4.2 Regional requirements.....                                            | 9  |
| 5 Operating bands and channel arrangement .....                           | 10 |
| 5.1 General .....                                                         | 10 |
| 5.2 Void.....                                                             | 10 |
| 5.3 Void.....                                                             | 10 |
| 5.4 Void.....                                                             | 10 |
| 5.5 Operating bands.....                                                  | 10 |
| 5.6 Channel bandwidth.....                                                | 10 |
| 5.7 Channel arrangement.....                                              | 11 |
| 5.7.1 Channel spacing.....                                                | 11 |
| 5.7.2 Channel raster.....                                                 | 11 |
| 5.7.3 Carrier frequency and EARFCN .....                                  | 11 |
| 6 Output power.....                                                       | 12 |
| 6.1 Minimum requirement.....                                              | 12 |
| 7 Frequency stability.....                                                | 13 |
| 7.1 Minimum requirement.....                                              | 13 |
| 8 Out of band gain.....                                                   | 13 |
| 8.1 Minimum requirement.....                                              | 13 |
| 9 Unwanted emissions .....                                                | 15 |
| 9.1 Operating band unwanted emissions.....                                | 15 |
| 9.1.1 Operating band unwanted emissions (Category A).....                 | 15 |
| 9.1.1.1 Minimum Requirements .....                                        | 15 |
| 9.1.2 Operating band unwanted emissions (Category B).....                 | 17 |
| 9.1.2.1 Minimum Requirement.....                                          | 17 |
| 9.1.2.1.1 Category B requirements (Option 1).....                         | 17 |
| 9.1.2.1.2 Category B requirements (Option 2).....                         | 20 |
| 9.1.3 Additional requirements .....                                       | 21 |
| 9.1.4 Protection of the BS receiver in the operating band.....            | 23 |
| 9.1.4.1 Minimum Requirement.....                                          | 24 |
| 9.2 Spurious emissions.....                                               | 24 |
| 9.2.1 Mandatory requirements.....                                         | 24 |
| 9.2.1.1 Spurious emissions (Category A) .....                             | 25 |
| 9.2.1.1.1 Minimum Requirement .....                                       | 25 |
| 9.2.1.2 Spurious emissions (Category B) .....                             | 25 |
| 9.2.1.2.1 Minimum Requirement .....                                       | 25 |
| 9.2.2 Co-existence with other systems in the same geographical area.....  | 25 |
| 9.2.2.1 Minimum requirement .....                                         | 26 |
| 9.2.3 Co-location with base stations.....                                 | 31 |
| 9.2.3.1 Minimum Requirements .....                                        | 31 |
| 10 Error Vector Magnitude .....                                           | 35 |
| 10.1 Downlink Error Vector Magnitude .....                                | 35 |
| 10.1.1 Minimum requirement.....                                           | 35 |
| 10.2 Uplink Error Vector Magnitude .....                                  | 36 |

|                             |                                                                   |           |
|-----------------------------|-------------------------------------------------------------------|-----------|
| 10.2.1                      | Minimum requirement.....                                          | 36        |
| 11                          | Input Intermodulation .....                                       | 36        |
| 11.1                        | General requirement.....                                          | 36        |
| 11.1.1                      | Minimum requirement.....                                          | 36        |
| 11.2                        | Co-location with BS in other systems.....                         | 36        |
| 11.2.1                      | Minimum requirement.....                                          | 37        |
| 11.3                        | Co-existence with other systems.....                              | 41        |
| 11.3.1                      | Minimum requirement.....                                          | 41        |
| 12                          | Output intermodulation .....                                      | 44        |
| 12.1                        | Minimum requirement.....                                          | 45        |
| 13                          | Adjacent Channel Rejection Ratio (ACRR) .....                     | 46        |
| 13.1                        | Definitions and applicability .....                               | 46        |
| 13.1.1                      | Minimum Requirements.....                                         | 46        |
| 13.2                        | Co-existence with UTRA.....                                       | 46        |
| 13.2.1.                     | Minimum Requirements.....                                         | 46        |
| <b>Annex A (normative):</b> | <b>Environmental requirements for the Repeater equipment.....</b> | <b>47</b> |
| Annex B (informative):      | Change history.....                                               | 48        |

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

The present document establishes the minimum RF characteristics of E-UTRA FDD Repeater.

# --- 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
  - For a specific reference, subsequent revisions do not apply.
  - For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.
- [1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".
- [2] ITU-R Recommendation SM.329, "Unwanted emissions in the spurious domain".
- [3] ITU-R Recommendation M.1545: "Measurement uncertainty as it applies to test limits for the terrestrial component of International Mobile Telecommunications-2000".
- [4] 3GPP TS 36.143: "Evolved Universal Terrestrial Radio Access (E-UTRA); FDD Repeater conformance testing"
- [5] 3GPP TR 25.942: "RF system scenarios".
- [6] 3GPP TS.36.104: "E-UTRA Base Station (BS) radio transmission and reception".
- [7] IEC 60721-3-3 (2002): "Classification of environmental conditions - Part 3: Classification of groups of environmental parameters and their severities - Section 3: Stationary use at weather protected locations".
- [8] IEC 60721-3-4 (1995): "Classification of environmental conditions - Part 3: Classification of groups of environmental parameters and their severities - Section 4: Stationary use at non-weather protected locations".

# --- 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

**Carrier:** The modulated waveform conveying the E-UTRA or UTRA physical channels

**Channel bandwidth:** The RF bandwidth supporting a single E-UTRA RF carrier with the transmission bandwidth configured in the uplink or downlink of a cell. The channel bandwidth is measured in MHz and is used as a reference for transmitter and receiver RF requirements.

**Channel edge:** The lowest and highest frequency of the E-UTRA carrier, separated by the channel bandwidth.

**Donor coupling loss:** is the coupling loss between the repeater and the donor base station.

**Downlink:** Signal path where base station transmits and mobile receives.

**Downlink operating band:** The part of the operating band designated for downlink.

**Maximum output power, Pmax:** This is the mean power level per carrier measured at the antenna connector of the Repeater in specified reference condition.

**Operating band:** A frequency range in which E-UTRA operates (paired or unpaired), that is defined with a specific set of technical requirements.

NOTE1: The operating band(s) for an E-UTRA Repeater is declared by the manufacturer according to the designations in clause 5.5 table 5.5-1.

NOTE2: Unless specified, operating band refers to the uplink operating band and downlink operating band.

**Output power, Pout:** This is the mean power of one carrier at maximum repeater gain delivered to a load with resistance equal to the nominal load impedance of the transmitter.

**Pass band:** The frequency range in which the repeater operates in with operational configuration. This frequency range can correspond to one or several consecutive nominal channels. If they are not consecutive each subset of channels shall be considered as an individual pass band. A repeater can have one or several pass bands.

**Rated output power:** Rated output power of the repeater is the mean power level per carrier that the manufacturer has declared to be available at the antenna connector.

**Repeater:** A device that receives, amplifies and transmits the radiated or conducted RF carrier both in the downlink direction (from the base station to the mobile area) and in the uplink direction (from the mobile to the base station)

**Transmission bandwidth:** Bandwidth of an instantaneous transmission from a UE or BS, measured in Resource Block units.

**Transmission bandwidth configuration:** The highest transmission bandwidth allowed for uplink or downlink in a given channel bandwidth, measured in Resource Block units.

**Uplink:** Signal path where mobile transmits and base station receives.

**Uplink operating band:** The part of the operating band designated for uplink.

## 3.2 Symbols

For the purposes of the present document, the following symbols apply:

|                       |                                                                                                                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BW <sub>Channel</sub> | Channel bandwidth                                                                                                                                                                                             |
| BW <sub>Config</sub>  | Transmission bandwidth configuration, expressed in MHz, where $BW_{Config} = N_{RB} \times 180 \text{ kHz}$ in the uplink and $BW_{Config} = 15 \text{ kHz} + N_{RB} \times 180 \text{ kHz}$ in the downlink. |
| BW <sub>Meas</sub>    | Measurement bandwidth                                                                                                                                                                                         |
| BW <sub>Signal</sub>  | Bandwidth of the repeater input signal filling the repeater pass band                                                                                                                                         |
| F <sub>DL_low</sub>   | The lowest frequency of the downlink operating band                                                                                                                                                           |
| F <sub>DL_high</sub>  | The highest frequency of the downlink operating band                                                                                                                                                          |
| F <sub>filter</sub>   | Filter centre frequency                                                                                                                                                                                       |
| F <sub>UL_low</sub>   | The lowest frequency of the uplink operating band                                                                                                                                                             |
| F <sub>UL_high</sub>  | The highest frequency of the uplink operating band                                                                                                                                                            |
| f_offset_PB           | Distance from the channel edge frequency of the first or last channel in the pass band                                                                                                                        |
| N <sub>DL</sub>       | Downlink EARFCN                                                                                                                                                                                               |
| N <sub>Offs-DL</sub>  | Offset used for calculating downlink EARFCN                                                                                                                                                                   |
| N <sub>Offs-UL</sub>  | Offset used for calculating uplink EARFCN                                                                                                                                                                     |
| N <sub>RB</sub>       | Transmission bandwidth configuration, expressed in units of resource blocks                                                                                                                                   |
| N <sub>UL</sub>       | Uplink EARFCN                                                                                                                                                                                                 |
| P <sub>EM,N</sub>     | Declared emission level for channel N                                                                                                                                                                         |
| P <sub>max</sub>      | Maximum output power                                                                                                                                                                                          |
| P <sub>out</sub>      | Output power                                                                                                                                                                                                  |

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

|        |                                                |
|--------|------------------------------------------------|
| ACRR   | Adjacent Channel Rejection Ratio               |
| BS     | Base Station                                   |
| DTT    | Digital Terrestrial Television                 |
| EARFCN | E-UTRA Absolute Radio Frequency Channel Number |
| EVM    | Error Vector Magnitude                         |
| IDFT   | Inverse Discrete Fourier Transform             |
| PB     | Pass Band                                      |
| TBD    | To Be Defined                                  |

# --- 4 General

## 4.1 Relationship between Minimum Requirements and Test Requirements

The Minimum Requirements given in this specification make no allowance for measurement uncertainty. The test specification TS 36.143 [4] Annex B defines Test Tolerances. These Test Tolerances are individually calculated for each test. The Test Tolerances are used to relax the Minimum Requirements in this specification to create Test Requirements.

The measurement results returned by the Test System are compared - without any modification - against the Test Requirements as defined by the shared risk principle.

The Shared Risk principle is defined in ITU-R M.1545 [3].

## 4.2 Regional requirements

Some requirements in the present document may only apply in certain regions either as optional requirements or set by local and regional regulation as mandatory requirements. It is normally not stated in the 3GPP specifications under what exact circumstances that the requirements apply, since this is defined by local or regional regulation.

Table 4.2-1 lists all requirements that may be applied differently in different regions.

**Table 4.2-1: List of regional requirements**

| Clause number | Requirement                                                                       | Comments                                                                                                                                                                                          |
|---------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5.5           | Operating bands                                                                   | Some bands may be applied regionally.                                                                                                                                                             |
| 5.6           | Channel bandwidth                                                                 | Some channel bandwidths may be applied regionally.                                                                                                                                                |
| 5.7           | Channel arrangement                                                               | The requirement is applied according to what operating bands in clause 5.5 that are supported by the Repeater.                                                                                    |
| 6.1           | Maximum output power                                                              | In certain regions, the minimum requirement for normal conditions may apply also for some conditions outside the range of conditions defined as normal.                                           |
| 9.1.1.1       | Operating band unwanted emissions (Category A)                                    | This requirement is mandatory for regions where Category A limits for spurious emissions, as defined in ITU-R Recommendation SM.329 [2] apply.                                                    |
| 9.1.2.1       | Operating band unwanted emissions (Category B)                                    | This requirement is mandatory for regions where Category B limits for spurious emissions, as defined in ITU-R Recommendation SM.329 [2], apply.                                                   |
| 9.1.3         | Operating band unwanted emissions : Additional requirements                       | These requirements may be applied regionally for some operating bands.                                                                                                                            |
| 9.2.1.1       | Spurious emissions (Category A)                                                   | This requirement is mandatory for regions where Category A limits for spurious emissions, as defined in ITU-R Recommendation SM.329 [2] apply.                                                    |
| 9.2.1.2       | Spurious emissions (Category B)                                                   | This requirement is mandatory for regions where Category B limits for spurious emissions, as defined in ITU-R Recommendation SM.329 [2], apply.                                                   |
| 9.2.2         | Spurious emissions: Co-existence with other systems in the same geographical area | These requirements may apply in geographic areas in which both E-UTRA –FDD repeater and a system operating in another frequency band are deployed.                                                |
| 9.2.3         | Spurious emissions: Co-location with base stations                                | These requirements may be applied for the protection of other BS receivers when a BS operating in another frequency band is co-located with an E-UTRA-FDD repeater.                               |
| 11.2          | Input Intermodulation: Co-location with BS in other systems                       | These requirements may be applied for the protection of FDD Repeater input when GSM900, DCS1800, PCS1900, GSM850, UTRA FDD, UTRA TDD and/or E-UTRA BS are co-located with an E-UTRA FDD Repeater. |
| 11.3          | Input Intermodulation: Co-existence with other systems                            | These requirements may be applied when GSM900, DCS1800, PCS1900, GSM850, UTRA FDD, UTRA TDD and/or E-UTRA BS operating in another frequency band co-exist with an E-UTRA FDD Repeater             |

# 5 Operating bands and channel arrangement

## 5.1 General

The channel arrangements presented in this clause are based on the operating bands and channel bandwidths defined in the present release of specifications.

NOTE: Other operating bands and channel bandwidths may be considered in future releases.

## 5.2 Void

## 5.3 Void

## 5.4 Void

## 5.5 Operating bands

E-UTRA FDD is designed to operate in the operating bands defined in Table 5.5-1.

**Table 5.5-1 E-UTRA operating bands**

| E-UTRA operating band | Uplink (UL) operating band                 | Downlink (DL) operating band               | Duplex Mode |
|-----------------------|--------------------------------------------|--------------------------------------------|-------------|
|                       | F <sub>UL_low</sub> – F <sub>UL_high</sub> | F <sub>DL_low</sub> – F <sub>DL_high</sub> |             |
| 1                     | 1920 MHz – 1980 MHz                        | 2110 MHz – 2170 MHz                        | FDD         |
| 2                     | 1850 MHz – 1910 MHz                        | 1930 MHz – 1990 MHz                        | FDD         |
| 3                     | 1710 MHz – 1785 MHz                        | 1805 MHz – 1880 MHz                        | FDD         |
| 4                     | 1710 MHz – 1755 MHz                        | 2110 MHz – 2155 MHz                        | FDD         |
| 5                     | 824 MHz – 849 MHz                          | 869 MHz – 894 MHz                          | FDD         |
| 6 <sup>1</sup>        | 830 MHz – 840 MHz                          | 875 MHz – 885 MHz                          | FDD         |
| 7                     | 2500 MHz – 2570 MHz                        | 2620 MHz – 2690 MHz                        | FDD         |
| 8                     | 880 MHz – 915 MHz                          | 925 MHz – 960 MHz                          | FDD         |
| 9                     | 1749.9 MHz – 1784.9 MHz                    | 1844.9 MHz – 1879.9 MHz                    | FDD         |
| 10                    | 1710 MHz – 1770 MHz                        | 2110 MHz – 2170 MHz                        | FDD         |
| 11                    | 1427.9 MHz – 1447.9 MHz                    | 1475.9 MHz – 1495.9 MHz                    | FDD         |
| 12                    | 698 MHz – 716 MHz                          | 728 MHz – 746 MHz                          | FDD         |
| 13                    | 777 MHz – 787 MHz                          | 746 MHz – 756 MHz                          | FDD         |
| 14                    | 788 MHz – 798 MHz                          | 758 MHz – 768 MHz                          | FDD         |
| 15                    | Reserved                                   | Reserved                                   |             |
| 16                    | Reserved                                   | Reserved                                   |             |
| 17                    | 704 MHz – 716 MHz                          | 734 MHz – 746 MHz                          | FDD         |
| 18                    | 815 MHz – 830 MHz                          | 860 MHz – 875 MHz                          | FDD         |
| 19                    | 830 MHz – 845 MHz                          | 875 MHz – 890 MHz                          | FDD         |
| 20                    | 832 MHz – 862 MHz                          | 791 MHz – 821 MHz                          | FDD         |
| 21                    | 1447.9 MHz – 1462.9 MHz                    | 1495.9 MHz – 1510.9 MHz                    | FDD         |
| 22                    | 3410 MHz – 3490 MHz                        | 3510 MHz – 3590 MHz                        | FDD         |
| 23                    | 2000 MHz – 2020 MHz                        | 2180 MHz – 2200 MHz                        | FDD         |
| 24                    | 1626.5 MHz – 1660.5 MHz                    | 1525 MHz – 1559 MHz                        | FDD         |
| 25                    | 1850 MHz – 1915 MHz                        | 1930 MHz – 1995 MHz                        | FDD         |

Note 1: Band 6 is not applicable.

## 5.6 Channel bandwidth

Requirements in present document are specified for the channel bandwidths listed in Table 5.6-1.

**Table 5.6-1 Transmission bandwidth configuration  $N_{RB}$  in E-UTRA channel bandwidths**

| Channel bandwidth<br>$BW_{Channel}$ [MHz]     | 1.4 | 3  | 5  | 10 | 15 | 20  |
|-----------------------------------------------|-----|----|----|----|----|-----|
| Transmission bandwidth configuration $N_{RB}$ | 6   | 15 | 25 | 50 | 75 | 100 |

Figure 5.6-1 shows the relation between the Channel bandwidth ( $BW_{Channel}$ ) and the Transmission bandwidth configuration ( $N_{RB}$ ). The channel edges are defined as the lowest and highest frequencies of the carrier separated by the channel bandwidth, i.e. at  $F_C \pm BW_{Channel} / 2$ .

![Figure 5.6-1: Definition of Channel Bandwidth and Transmission Bandwidth Configuration for one E-UTRA carrier. The diagram shows a carrier with a total Channel Bandwidth [MHz] indicated by a top double-headed arrow. Below it, the Transmission Bandwidth Configuration [RB] is shown as a narrower double-headed arrow. The Transmission Bandwidth [RB] is further indicated by a third double-headed arrow. The carrier is divided into Resource blocks, with a group of Active Resource Blocks highlighted in blue. A dashed line marks the Center subcarrier (corresponds to DC in baseband) which is not transmitted in downlink. The Channel edge is marked at the far left and right of the carrier.](5e92d9e8e9ce204e405bff2367f88176_img.jpg)

Figure 5.6-1: Definition of Channel Bandwidth and Transmission Bandwidth Configuration for one E-UTRA carrier. The diagram shows a carrier with a total Channel Bandwidth [MHz] indicated by a top double-headed arrow. Below it, the Transmission Bandwidth Configuration [RB] is shown as a narrower double-headed arrow. The Transmission Bandwidth [RB] is further indicated by a third double-headed arrow. The carrier is divided into Resource blocks, with a group of Active Resource Blocks highlighted in blue. A dashed line marks the Center subcarrier (corresponds to DC in baseband) which is not transmitted in downlink. The Channel edge is marked at the far left and right of the carrier.

**Figure 5.6-1 Definition of Channel Bandwidth and Transmission Bandwidth Configuration for one E-UTRA carrier**

## 5.7 Channel arrangement

### 5.7.1 Channel spacing

The spacing between carriers will depend on the deployment scenario, the size of the frequency block available and the channel bandwidths. The nominal channel spacing between two adjacent E-UTRA carriers is defined as following:

$$\text{Nominal Channel spacing} = (BW_{Channel(1)} + BW_{Channel(2)})/2$$

where  $BW_{Channel(1)}$  and  $BW_{Channel(2)}$  are the channel bandwidths of the two respective E-UTRA carriers. The channel spacing can be adjusted to optimize performance in a particular deployment scenario.

### 5.7.2 Channel raster

The channel raster is 100 kHz for all bands, which means that the carrier centre frequency must be an integer multiple of 100 kHz.

### 5.7.3 Carrier frequency and EARFCN

The carrier frequency in the uplink and downlink is designated by the E-UTRA Absolute Radio Frequency Channel Number (EARFCN) in the range 0 - 65535. The relation between EARFCN and the carrier frequency in MHz for the downlink is given by the following equation, where  $F_{DL\_low}$  and  $N_{offs-DL}$  are given in table 5.7.3-1 and  $N_{DL}$  is the downlink EARFCN.

$$F_{DL} = F_{DL\_low} + 0.1(N_{DL} - N_{offs-DL})$$

The relation between EARFCN and the carrier frequency in MHz for the uplink is given by the following equation where  $F_{UL\_low}$  and  $N_{Offs-UL}$  are given in table 5.7.3-1 and  $N_{UL}$  is the uplink EARFCN.

$$F_{UL} = F_{UL\_low} + 0.1(N_{UL} - N_{Offs-UL})$$

**Table 5.7.3-1 E-UTRA channel numbers**

| E-UTRA operating band | Downlink            |               |                   | Uplink              |               |                   |
|-----------------------|---------------------|---------------|-------------------|---------------------|---------------|-------------------|
|                       | $F_{DL\_low}$ [MHz] | $N_{Offs-DL}$ | Range of $N_{DL}$ | $F_{UL\_low}$ [MHz] | $N_{Offs-UL}$ | Range of $N_{UL}$ |
| 1                     | 2110                | 0             | 0 – 599           | 1920                | 18000         | 18000 – 18599     |
| 2                     | 1930                | 600           | 600 – 1199        | 1850                | 18600         | 18600 – 19199     |
| 3                     | 1805                | 1200          | 1200 – 1949       | 1710                | 19200         | 19200 – 19949     |
| 4                     | 2110                | 1950          | 1950 – 2399       | 1710                | 19950         | 19950 – 20399     |
| 5                     | 869                 | 2400          | 2400 – 2649       | 824                 | 20400         | 20400 – 20649     |
| 6                     | 875                 | 2650          | 2650 – 2749       | 830                 | 20650         | 20650 – 20749     |
| 7                     | 2620                | 2750          | 2750 – 3449       | 2500                | 20750         | 20750 – 21449     |
| 8                     | 925                 | 3450          | 3450 – 3799       | 880                 | 21450         | 21450 – 21799     |
| 9                     | 1844.9              | 3800          | 3800 – 4149       | 1749.9              | 21800         | 21800 – 22149     |
| 10                    | 2110                | 4150          | 4150 – 4749       | 1710                | 22150         | 22150 – 22749     |
| 11                    | 1475.9              | 4750          | 4750 – 4999       | 1427.9              | 22750         | 22750 – 22999     |
| 12                    | 728                 | 5000          | 5000 – 5179       | 698                 | 23000         | 23000 – 23179     |
| 13                    | 746                 | 5180          | 5180 – 5279       | 777                 | 23180         | 23180 – 23279     |
| 14                    | 758                 | 5280          | 5280 – 5379       | 788                 | 23280         | 23280 – 23379     |
| 15                    | Reserved            |               |                   | Reserved            |               |                   |
| 16                    | Reserved            |               |                   | Reserved            |               |                   |
| 17                    | 734                 | 5730          | 5730 – 5849       | 704                 | 23730         | 23730 – 23849     |
| 18                    | 860                 | 5850          | 5850 – 5999       | 815                 | 23850         | 23850 – 23999     |
| 19                    | 875                 | 6000          | 6000 – 6149       | 830                 | 24000         | 24000 – 24149     |
| 20                    | 791                 | 6150          | 6150 – 6449       | 832                 | 24150         | 24150 – 24449     |
| 21                    | 1495.9              | 6450          | 6450 – 6599       | 1447.9              | 24450         | 24450 – 24599     |
| 22                    | 3510                | 6600          | 6600 – 7399       | 3410                | 24600         | 24600 – 25399     |
| 23                    | 2180                | 7500          | 7500 – 7699       | 2000                | 25500         | 25500 – 25699     |
| 24                    | 1525                | 7700          | 7700 – 8039       | 1626.5              | 25700         | 25700 – 26039     |
| 25                    | 1930                | 8040          | 8040 – 8689       | 1850                | 26040         | 26040 – 26689     |

NOTE: The channel numbers that designate carrier frequencies so close to the operating band edges that the carrier extends beyond the operating band edge shall not be used. This implies that the first 7, 15, 25, 50, 75 and 100 channel numbers at the lower operating band edge and the last 6, 14, 24, 49, 74 and 99 channel numbers at the upper operating band edge shall not be used for channel bandwidths of 1.4, 3, 5, 10, 15 and 20 MHz respectively.

# 6 Output power

Output power,  $P_{out}$ , of the repeater is the mean power of one carrier at maximum repeater gain delivered to a load with resistance equal to the nominal load impedance of the transmitter.

Maximum output power,  $P_{max}$ , of the repeater is the mean power level per carrier measured at the antenna connector in a specified reference condition.

## 6.1 Minimum requirement

The requirements shall apply at maximum gain, with E-UTRA signals in the pass band of the repeater, at levels that produce the maximum rated output power per channel.

When the power of all signals is increased by 10 dB, compared to the power level that produce the maximum rated output power, the requirements shall still be met.

In normal conditions, the Repeater maximum output power shall remain within limits specified in Table 6.1-1 relative to the manufacturer's rated output power.

**Table 6.1-1: Repeater output power; normal conditions**

| <b>Rated output power</b> | <b>Limit</b>    |
|---------------------------|-----------------|
| $P \geq 31$ dBm           | +2 dB and -2 dB |
| $P < 31$ dBm              | +3 dB and -3 dB |

In extreme conditions, the Repeater maximum output power shall remain within the limits specified in Table 6.1-2 relative to the manufacturer's rated output power.

**Table 6.1-2: Repeater output power; extreme conditions**

| <b>Rated output power</b> | <b>Limit</b>        |
|---------------------------|---------------------|
| $P \geq 31$ dBm           | +2,5 dB and -2,5 dB |
| $P < 31$ dBm              | +4 dB and -4 dB     |

In certain regions, the minimum requirement for normal conditions may apply also for some conditions outside the ranges of conditions defined as normal.

# 7 Frequency stability

Frequency stability is the ability to maintain the same frequency on the output signal with respect to the input signal.

## 7.1 Minimum requirement

The frequency deviation of the output signal with respect to the input signal shall be no more than  $\pm 0,01$  PPM.

# 8 Out of band gain

Out of band gain refers to the gain of the repeater outside the pass band.

## 8.1 Minimum requirement

The intended use of a repeater in a system is to amplify the in band signals and not to amplify the out of band emission of the donor base station.

In the intended application of the repeater, the out of band gain is less than the donor coupling loss.

The repeater minimum donor coupling loss shall be declared by the manufacturer. This is the minimum required attenuation between the donor BS and the repeater for proper repeater operation.

The gain outside the pass band shall not exceed the maximum level specified in table 8.1-1, where:

- $f\_offset\_CW$  is the offset between the outer channel edge frequency of the outer channel in the pass band and a CW signal.

**Table 8.1-1: Out of band gain limits 1**

| <b>Frequency offset, <math>f\_offset\_CW</math></b> | <b>Maximum gain</b> |
|-----------------------------------------------------|---------------------|
| $0,2 \leq f\_offset\_CW < 1,0$ MHz                  | 60 dB               |
| $1,0 \leq f\_offset\_CW < 5,0$ MHz                  | 45 dB               |
| $5,0 \leq f\_offset\_CW < 10,0$ MHz                 | 45 dB               |
| $10,0$ MHz $\leq f\_offset\_CW$                     | 35 dB               |

For  $10,0$  MHz  $\leq f\_offset\_CW$  the out of band gain shall not exceed the maximum gain of table 8.1-2 or the maximum gain stated in table 8.1-1 whichever is lower.

**Table 8.1-2: Out of band gain limits 2**

| <b>Frequency offset, <math>f\_offset\_CW</math></b> | <b>Maximum gain</b>                                 |
|-----------------------------------------------------|-----------------------------------------------------|
| $10$ MHz $\leq f\_offset\_CW$                       | Out of band gain $\leq$ minimum donor coupling loss |

# 9 Unwanted emissions

Unwanted emissions consist of out-of-band emissions and spurious emissions [2]. Out of band emissions are unwanted emissions immediately outside the pass band bandwidth resulting from the modulation process and non-linearity in the transmitter, but excluding spurious emissions. Spurious emissions are emissions which are caused by unwanted transmitter effects such as harmonics emission, parasitic emission, intermodulation products and frequency conversion products, but exclude out of band emissions.

The out-of-band emissions requirement for repeater is specified both in terms operating band unwanted emissions and protection of the BS receiver in the uplink operating band. The Operating band unwanted emissions define all unwanted emissions in the repeater operating band plus the frequency ranges 10 MHz above and 10 MHz below that band. Unwanted emissions outside of this frequency range are limited by a spurious emissions requirement.

## 9.1 Operating band unwanted emissions

The Operating band unwanted emission limits are defined from 10 MHz below the lowest frequency of the repeater operating band up to 10 MHz above the highest frequency of the repeater operating band.

The requirements shall apply whatever the type of repeater considered (single carrier or multi-carrier) and for all configurations foreseen by the manufacturer's specification.

Emissions shall not exceed the maximum levels specified in the tables below, where:

- $\Delta f$  is the separation between the nominal pass band edge frequency and the nominal -3dB point of the measuring filter closest to the carrier frequency.
- $BW_{Meas}$  is the measurement bandwidth.
- $BW_{Pass\ band}$  is the bandwidth of the repeater's pass band.
- $f\_offset$  is the separation between the nominal pass band edge frequency and the centre of the measuring filter.
- $f\_offset_{max}$  is the offset to the frequency 10 MHz outside the repeater operating band.
- $\Delta f_{max}$  is equal to  $f\_offset_{max}$  minus half of the bandwidth of the measuring filter.

The requirements of either subclause 9.1.1 (Category A limits) or subclause 9.1.2 (Category B limits) shall apply. The application of either Category A or Category B limits shall be the same as for spurious emissions (Mandatory Requirements) in subclause 9.2.1.

The Additional operating band unwanted emission limits defined in subclause 9.1.3 below may be mandatory in certain regions. In other regions it may not apply.

Unless otherwise stated, all requirements are measured as mean power (RMS).

### 9.1.1 Operating band unwanted emissions (Category A)

#### 9.1.1.1 Minimum Requirements

This requirement applies to the uplink and downlink of the repeater, at maximum gain, and with the following input signals:

- without E-UTRA input signal
- with E-UTRA input signals in the pass band of the repeater, at levels that produce the maximum rated power output per channel
- with 10 dB increased E-UTRA input signals in all channels in the pass band, compared to the input level producing the maximum rated output power.

For E-UTRA FDD repeater operating in Bands 5, 6, 8, 12, 13, 14, 17, 18 and 19 emissions shall not exceed the maximum levels specified in Tables 9.1.1.1-1 and 9.1.1.1-2.

**Table 9.1.1.1-1: General operating band unwanted emission limits for repeater pass band bandwidth lower than 5 MHz (E-UTRA bands <1GHz) for Category A**

| Frequency offset of measurement filter -3dB point, $\Delta f$                   | Frequency offset of measurement filter centre frequency, $f\_offset$                                                                     | Minimum requirement                                                                                                                                                                                                                                                               | Measurement bandwidth |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < \text{BW}_{\text{Pass band}}$                    | $\text{BW}_{\text{Meas}}/2 \leq f\_offset < \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$                                    | $\text{Max}[-2.1875 * \text{BW}_{\text{Passband}} + 2.0625; -1.25 * \text{BW}_{\text{Passband}} - 0.75]\text{dBm} + \frac{\text{Max}[-10; \text{BW}_{\text{Passband}} - 12]}{\text{BW}_{\text{Passband}}} * \left(f\_offset - \frac{\text{BW}_{\text{meas}}}{2}\right) \text{dB}$ | 100 kHz               |
| $\text{BW}_{\text{Pass band}} \leq \Delta f < 2 * \text{BW}_{\text{Pass band}}$ | $\text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < 2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$ | $\text{Max}[-1.43 * \text{BW}_{\text{Passband}} - 9.0; -0.45 * \text{BW}_{\text{Passband}} - 11.73]\text{dBm}$                                                                                                                                                                    | 100 kHz               |
| $2 * \text{BW}_{\text{Pass band}} \leq \Delta f \leq \Delta f_{\text{max}}$     | $2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < f\_offset_{\text{max}}$                                   | -13 dBm                                                                                                                                                                                                                                                                           | 100 kHz               |

Note: Frequencies and bandwidth are given in MHz.

**Table 9.1.1.1-2: General operating band unwanted emission limits for repeater pass band bandwidth 5 MHz and above (E-UTRA bands <1GHz) for Category A**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                              | Measurement bandwidth (Note 1) |
|---------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------|
| $0 \text{ MHz} \leq \Delta f < 5 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 5.05 \text{ MHz}$                 | $-7 \text{ dBm} - \frac{7}{5} \cdot \left(\frac{f\_offset}{\text{MHz}} - 0.05\right) \text{ dB}$ | 100 kHz                        |
| $5 \text{ MHz} \leq \Delta f < 10 \text{ MHz}$                | $5.05 \text{ MHz} \leq f\_offset < 10.05 \text{ MHz}$                | -14 dBm                                                                                          | 100 kHz                        |
| $10 \text{ MHz} \leq \Delta f \leq \Delta f_{\text{max}}$     | $10.05 \text{ MHz} \leq f\_offset < f\_offset_{\text{max}}$          | -13 dBm                                                                                          | 100 kHz                        |

Note: Frequencies and bandwidth are given in MHz.

For E-UTRA FDD repeaters operating in Bands 1, 2, 3, 4, 7, 9, 10, 11, 21, 22, 23, 24 and 25 emissions shall not exceed the maximum levels specified in Tables 9.1.1.1-3 and 9.1.1.1-4:

**Table 9.1.1.1-3: General operating band unwanted emission limits for repeater pass band bandwidth lower than 5 MHz (E-UTRA bands >1GHz) for Category A**

| Frequency offset of measurement filter -3dB point, $\Delta f$                   | Frequency offset of measurement filter centre frequency, $f\_offset$                                                                     | Minimum requirement                                                                                                                                                                                                                                                           | Measurement bandwidth |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < \text{BW}_{\text{Pass band}}$                    | $\text{BW}_{\text{Meas}}/2 \leq f\_offset < \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$                                    | $\text{Max}[-2.5 * \text{BW}_{\text{Passband}} + 2.5; -1 * \text{BW}_{\text{Passband}} - 2]\text{dBm} + \frac{\text{Max}[-10; 1.5 * \text{BW}_{\text{Passband}} - 14.5]}{\text{BW}_{\text{Passband}}} * \left(f\_offset - \frac{\text{BW}_{\text{meas}}}{2}\right) \text{dB}$ | 100 kHz               |
| $\text{BW}_{\text{Pass band}} \leq \Delta f < 2 * \text{BW}_{\text{Pass band}}$ | $\text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < 2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$ | $\text{Max}[-2.5 * \text{BW}_{\text{Passband}} - 7.5; 0.5 * \text{BW}_{\text{Passband}} - 16.5]\text{dBm}$                                                                                                                                                                    | 100 kHz               |
| $2 * \text{BW}_{\text{Pass band}} \leq \Delta f \leq \Delta f_{\text{max}}$     | $2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < f\_offset_{\text{max}}$                                   | -13 dBm                                                                                                                                                                                                                                                                       | 1MHz                  |

Note: Frequencies and bandwidth are given in MHz.

**Table 9.1.1.1-4: General operating band unwanted emission limits for repeater pass band bandwidth 5 MHz and above (E-UTRA bands >1GHz) for Category A**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                                | Measurement bandwidth (Note 1) |
|---------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------|
| $0 \text{ MHz} \leq \Delta f < 5 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 5.05 \text{ MHz}$                 | $-7 \text{ dBm} - \frac{7}{5} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz                        |
| $5 \text{ MHz} \leq \Delta f < 10 \text{ MHz}$                | $5.05 \text{ MHz} \leq f\_offset < 10.05 \text{ MHz}$                | -14 dBm                                                                                            | 100 kHz                        |
| $10 \text{ MHz} \leq \Delta f \leq \Delta f_{\max}$           | $10.5 \text{ MHz} \leq f\_offset < f\_offset_{\max}$                 | -13 dBm                                                                                            | 1MHz                           |
| Note: Frequencies and bandwidth are given in MHz.             |                                                                      |                                                                                                    |                                |

### 9.1.2 Operating band unwanted emissions (Category B)

#### 9.1.2.1 Minimum Requirement

For Category B Operating band unwanted emissions, there are two options for the limits that may be applied regionally. Either the limits in subclause 9.1.2.1.1 or subclause 9.1.2.1.2 shall be applied.

This requirement applies to the uplink and downlink of the repeater, at maximum gain, and with the following input signals:

- without E-UTRA input signal
- with E-UTRA input signals in the pass band of the repeater, at levels that produce the maximum rated power output per channel
- with 10 dB increased E-UTRA input signals in all channels in the pass band, compared to the input level producing the maximum rated output power.

##### 9.1.2.1.1 Category B requirements (Option 1)

For E-UTRA FDD repeater operating in Bands 5, 6, 8, 12, 13, 14, 17 and 20 emissions shall not exceed the maximum levels specified in Tables 9.1.2.1.1-1 and 9.1.2.1.1-2:

**Table 9.1.2.1.1-1: General operating band unwanted emission limits for repeater pass band bandwidth lower than 5 MHz (E-UTRA bands <1GHz) for Category B**

| Frequency offset of measurement filter -3dB point, $\Delta f$                                                                                                                                                                                                                                                | Frequency offset of measurement filter centre frequency, $f\_offset$                                                                     | Minimum requirement                                                                                                                                                                                                                                                                                 | Measurement bandwidth |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < \text{BW}_{\text{Pass band}}$                                                                                                                                                                                                                                                 | $\text{BW}_{\text{Meas}}/2 \leq f\_offset < \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$                                    | EMBED Equation.3 $\text{Max}[-2.5 * \text{BW}_{\text{Passband}} + 2.5; -1 * \text{BW}_{\text{Passband}} - 2] \text{ dBm} + \frac{\text{Max}[-10; 1.5 * \text{BW}_{\text{Passband}} - 14.5]}{\text{BW}_{\text{Passband}}} * \left( f\_offset - \frac{\text{BW}_{\text{Meas}}}{2} \right) \text{ dB}$ | 100 kHz               |
| $\text{BW}_{\text{Pass band}} \leq \Delta f < 2 * \text{BW}_{\text{Pass band}}$                                                                                                                                                                                                                              | $\text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < 2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$ | $\text{Max}[-2.5 * \text{BW}_{\text{Passband}} - 7.5; 0.5 * \text{BW}_{\text{Passband}} - 16.5] \text{ dBm}$                                                                                                                                                                                        | 100 kHz               |
| $2 * \text{BW}_{\text{Pass band}} \leq \Delta f \leq \Delta f_{\max}$                                                                                                                                                                                                                                        | $2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < f\_offset_{\max}$                                         | -16 dBm                                                                                                                                                                                                                                                                                             | 100 kHz               |
| NOTE 1: Frequencies and bandwidth are given in MHz.                                                                                                                                                                                                                                                          |                                                                                                                                          |                                                                                                                                                                                                                                                                                                     |                       |
| NOTE 2: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 1.4 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-3 supersedes Table 9.1.2.1.1-1 and Table 9.1.2.1.1-2 for applicable frequency offsets. |                                                                                                                                          |                                                                                                                                                                                                                                                                                                     |                       |
| NOTE 3: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 3 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-4 supersedes Table 9.1.2.1.1-1 and Table 9.1.2.1.1-2 for applicable frequency offsets.   |                                                                                                                                          |                                                                                                                                                                                                                                                                                                     |                       |

**Table 9.1.2.1.1-2: General operating band unwanted emission limits for repeater pass band bandwidth 5 MHz and above (E-UTRA bands <1GHz) for Category B**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                                | Measurement bandwidth (Note 1) |
|---------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------|
| $0 \text{ MHz} \leq \Delta f < 5 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 5.05 \text{ MHz}$                 | $-7 \text{ dBm} - \frac{7}{5} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz                        |
| $5 \text{ MHz} \leq \Delta f < 10 \text{ MHz}$                | $5.05 \text{ MHz} \leq f\_offset < 10.05 \text{ MHz}$                | -14 dBm                                                                                            | 100 kHz                        |
| $10 \text{ MHz} \leq \Delta f \leq \Delta f_{\max}$           | $10.05 \text{ MHz} \leq f\_offset < f\_offset_{\max}$                | -16 dBm                                                                                            | 100 kHz                        |

NOTE 1: Frequencies and bandwidth are given in MHz.  
NOTE 2: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 1.4 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-3 supersedes Table 9.1.2.1.1-1 and Table 9.1.2.1.1-2 for applicable frequency offsets.  
NOTE 3: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 3 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-4 supersedes Table 9.1.2.1.1-1 and Table 9.1.2.1.1-2 for applicable frequency offsets.

**Table 9.1.2.1.1-3: Conditional operating band unwanted emission limits for repeater input signal bandwidth of 1.4 MHz**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                                   | Measurement bandwidth |
|---------------------------------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 1.05 \text{ MHz}$              | $0.05 \text{ MHz} \leq f\_offset < 1.1 \text{ MHz}$                  | $-1 \text{ dBm} - \frac{10}{1.4} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz               |

Note: Frequencies and bandwidth are given in MHz

**Table 9.1.2.1.1-4: Conditional operating band unwanted emission limits for repeater input signal bandwidth of 3 MHz**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                                 | Measurement bandwidth |
|---------------------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 1.05 \text{ MHz}$              | $0.05 \text{ MHz} \leq f\_offset < 1.1 \text{ MHz}$                  | $-5 \text{ dBm} - \frac{10}{3} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz               |

Note: Frequencies and bandwidth are given in MHz

For E-UTRA FDD repeater operating in Bands 1, 2, 3, 4, 7, 9, 10, 22 and 25 emissions shall not exceed the maximum levels specified in Tables 9.1.2.1.1-5 and 9.1.2.1.1-6:

**Table 9.1.2.1.1-5: General operating band unwanted emission limits for repeater pass band bandwidth lower than 5 MHz (E-UTRA bands >1GHz) for Category B**

| Frequency offset of measurement filter -3dB point, $\Delta f$                   | Frequency offset of measurement filter centre frequency, $f\_offset$                                                                     | Minimum requirement                                                                                                                                                                                                                                                                | Measurement bandwidth |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < \text{BW}_{\text{Pass band}}$                    | $\text{BW}_{\text{Meas}}/2 \leq f\_offset < \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$                                    | $\text{Max}[-2.5 * \text{BW}_{\text{Passband}} + 2.5; -1 * \text{BW}_{\text{Passband}} - 2] \text{ dBm} + \frac{\text{Max}[-10; 1.5 * \text{BW}_{\text{Passband}} - 14.5]}{\text{BW}_{\text{Passband}}} * \left( f\_offset - \frac{\text{BW}_{\text{Meas}}}{2} \right) \text{ dB}$ | 100 kHz               |
| $\text{BW}_{\text{Pass band}} \leq \Delta f < 2 * \text{BW}_{\text{Pass band}}$ | $\text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < 2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2$ | $\text{Max}[-2.5 * \text{BW}_{\text{Passband}} - 7.5; 0.5 * \text{BW}_{\text{Passband}} - 16.5] \text{ dBm}$                                                                                                                                                                       | 100 kHz               |
| $2 * \text{BW}_{\text{Pass band}} \leq \Delta f \leq \Delta f_{\text{max}}$     | $2 * \text{BW}_{\text{Pass band}} + \text{BW}_{\text{Meas}}/2 \leq f\_offset < f\_offset_{\text{max}}$                                   | -15 dBm                                                                                                                                                                                                                                                                            | 1MHz                  |

NOTE 1: Frequencies and bandwidth are given in MHz.  
NOTE 2: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 1.4 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-7 supersedes Table 9.1.2.1.1-5 and Table 9.1.2.1.1-6 for applicable frequency offsets.  
NOTE 3: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 3 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-8 supersedes Table 9.1.2.1.1-5 and Table 9.1.2.1.1-6 for applicable frequency offsets.

**Table 9.1.2.1.1-6: General operating band unwanted emission limits for repeater pass band bandwidth 5 MHz and above (E-UTRA bands >1GHz) for Category B**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                                | Measurement bandwidth (Note 1) |
|---------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------|
| $0 \text{ MHz} \leq \Delta f < 5 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 5.05 \text{ MHz}$                 | $-7 \text{ dBm} - \frac{7}{5} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz                        |
| $5 \text{ MHz} \leq \Delta f < 10 \text{ MHz}$                | $5.05 \text{ MHz} \leq f\_offset < 10.05 \text{ MHz}$                | -14 dBm                                                                                            | 100 kHz                        |
| $10 \text{ MHz} \leq \Delta f \leq \Delta f_{\text{max}}$     | $10.5 \text{ MHz} \leq f\_offset < f\_offset_{\text{max}}$           | -15 dBm                                                                                            | 1MHz                           |

NOTE 1: Frequencies and bandwidth are given in MHz.  
NOTE 2: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 1.4 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-7 supersedes Table 9.1.2.1.1-5 and Table 9.1.2.1.1-6 for applicable frequency offsets.  
NOTE 3: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 3 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.1-8 supersedes Table 9.1.2.1.1-5 and Table 9.1.2.1.1-6 for applicable frequency offsets.

**Table 9.1.2.1.1-7: Conditional operating band unwanted emission limits for repeater input signal bandwidth of 1.4 MHz**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                                   | Measurement bandwidth |
|---------------------------------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 1.05 \text{ MHz}$              | $0.05 \text{ MHz} \leq f\_offset < 1.1 \text{ MHz}$                  | $-1 \text{ dBm} - \frac{10}{1.4} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz               |

Note: Frequencies and bandwidth are given in MHz

**Table 9.1.2.1.1-8: Conditional operating band unwanted emission limits for repeater input signal bandwidth of 3 MHz**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                               | Measurement bandwidth |
|---------------------------------------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 1.05 \text{ MHz}$              | $0.05 \text{ MHz} \leq f\_offset < 1.1 \text{ MHz}$                  | $-5\text{dBm} - \frac{10}{3} \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.05 \right) \text{ dB}$ | 100 kHz               |
| Note: Frequencies and bandwidth are given in MHz              |                                                                      |                                                                                                   |                       |

##### 9.1.2.1.2 Category B requirements (Option 2)

The limits in this subclause are intended for Europe and may be applied regionally for E-UTRA FDD Repeater operating in band 3 and 8.

For E-UTRA FDD repeater operating in Bands 3 and 8 emissions shall not exceed the maximum levels specified in Tables 9.1.2.1.2-1 and 9.1.2.1.2-2:

**Table 9.1.2.1.2-1: General operating band unwanted emission limits for repeater pass band lower than 5 MHz**

| Frequency offset of measurement filter -3dB point, $\Delta f$                                                                                                                                                                                                                                   | Frequency offset of measurement filter centre frequency, $f\_offset$                             | Minimum requirement                                                                       | Measurement bandwidth |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 0.2 \text{ MHz}$                                                                                                                                                                                                                                                 | $0.015 \text{ MHz} \leq f\_offset < 0.215 \text{ MHz}$                                           | -14 dBm                                                                                   | 30 kHz                |
| $0.2 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                                                                                                                                                                                                                                                 | $0.215 \text{ MHz} \leq f\_offset < 1.015 \text{ MHz}$                                           | $-14\text{dBm} - 15 \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.215 \right) \text{ dB}$ | 30 kHz                |
| (Note 3)                                                                                                                                                                                                                                                                                        | $1.015 \text{ MHz} \leq f\_offset < 1.5 \text{ MHz}$                                             | -26 dBm                                                                                   | 30 kHz                |
| $1 \text{ MHz} \leq \Delta f < 2 \cdot \text{BW}_{\text{Pass band}}$                                                                                                                                                                                                                            | $1.5 \text{ MHz} \leq f\_offset < 2 \cdot \text{BW}_{\text{Pass band}} + 0.5 \text{ MHz}$        | -13 dBm                                                                                   | 1 MHz                 |
| $2 \cdot \text{BW}_{\text{Pass band}} \leq \Delta f \leq \Delta f_{\text{max}}$                                                                                                                                                                                                                 | $2 \cdot \text{BW}_{\text{Pass band}} + 0.5 \text{ MHz} \leq f\_offset < f\_offset_{\text{max}}$ | -15 dBm                                                                                   | 1 MHz                 |
| NOTE 1: Frequencies and bandwidth are given in MHz.                                                                                                                                                                                                                                             |                                                                                                  |                                                                                           |                       |
| NOTE 2: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 1.4 MHz or 3 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.2-3 supersedes Table 9.1.2.1.2-1 for applicable frequency offsets. |                                                                                                  |                                                                                           |                       |
| NOTE 3: This frequency range ensures that the range of values of $f\_offset$ is continuous                                                                                                                                                                                                      |                                                                                                  |                                                                                           |                       |

**Table 9.1.2.1.2-2: General operating band unwanted emission limits for repeater pass band 5 MHz and above**

| Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                         | Measurement bandwidth |
|---------------------------------------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 0.2 \text{ MHz}$               | $0.015 \text{ MHz} \leq f\_offset < 0.215 \text{ MHz}$               | -14 dBm                                                                                     | 30 kHz                |
| $0.2 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$               | $0.215 \text{ MHz} \leq f\_offset < 1.015 \text{ MHz}$               | $-14 \text{ dBm} - 15 \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.215 \right) \text{ dB}$ | 30 kHz                |
| (Note 3)                                                      | $1.015 \text{ MHz} \leq f\_offset < 1.5 \text{ MHz}$                 | -26 dBm                                                                                     | 30 kHz                |
| $1 \text{ MHz} \leq \Delta f < 10 \text{ MHz}$                | $1.5 \text{ MHz} \leq f\_offset < 10.5 \text{ MHz}$                  | -13 dBm                                                                                     | 1 MHz                 |
| $10 \text{ MHz} \leq \Delta f \leq \Delta f_{\max}$           | $10.5 \text{ MHz} \leq f\_offset < f\_offset_{\max}$                 | -15 dBm                                                                                     | 1 MHz                 |

NOTE 1: Frequencies and bandwidth are given in MHz.  
NOTE 2: If the repeater input signal consists of E-UTRA signals with a channel bandwidth of 1.4 MHz or 3 MHz placed so that the channel edge is less than 200 kHz from the pass band edge, the requirements in Table 9.1.2.1.2-3 supersedes Table 9.1.2.1.2-2 for applicable frequency offsets.  
NOTE 3: This frequency range ensures that the range of values of  $f\_offset$  is continuous

**Table 9.1.2.1.2-3: Conditional operating band unwanted emission limits**

| Frequency offset of measurement filter -3 dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement                                                                        | Measurement bandwidth |
|----------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------|
| $0 \text{ MHz} \leq \Delta f < 0.05 \text{ MHz}$               | $0.015 \text{ MHz} \leq f\_offset < 0.065 \text{ MHz}$               | $5 \text{ dBm} - 60 \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.015 \right) \text{ dB}$  | 30 kHz                |
| $0.05 \text{ MHz} \leq \Delta f < 0.15 \text{ MHz}$            | $0.065 \text{ MHz} \leq f\_offset < 0.165 \text{ MHz}$               | $2 \text{ dBm} - 160 \cdot \left( \frac{f\_offset}{\text{MHz}} - 0.065 \right) \text{ dB}$ | 30 kHz                |
| $0.15 \text{ MHz} \leq \Delta f < 0.2 \text{ MHz}$             | $0.165 \text{ MHz} \leq f\_offset < 0.215 \text{ MHz}$               | -14 dBm                                                                                    | 30 kHz                |

NOTE: Frequencies and bandwidth are given in MHz.

### 9.1.3 Additional requirements

These requirements may be applied for the protection of other systems operating inside or near the E-UTRA Repeater downlink operating band. The limits may apply as an optional protection of such systems that are deployed in the same geographical area as the E-UTRA, or they may be set by local or regional regulation as a mandatory requirement for an E-UTRA operating band. It is in some cases not stated in the present document whether a requirement is mandatory or under what exact circumstances that a limit applies, since this is set by local or regional regulation. An overview of regional requirements in the present document is given in subclause 4.2.

In certain regions the following requirement may apply. For E-UTRA FDD repeaters operating in Band 5, emissions shall not exceed the maximum levels specified in Table 9.1.3-1.

**Table 9.1.3-1: Additional operating band unwanted emission limits for E-UTRA bands <1GHz**

| Input signal bandwidth | Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement | Measurement bandwidth (Note 1) |
|------------------------|---------------------------------------------------------------|----------------------------------------------------------------------|---------------------|--------------------------------|
| 1.4 MHz                | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.005 \text{ MHz} \leq f\_offset < 0.995 \text{ MHz}$               | -14 dBm             | 10 kHz                         |
| 3 MHz                  | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.015 \text{ MHz} \leq f\_offset < 0.985 \text{ MHz}$               | -13 dBm             | 30 kHz                         |
| 5 MHz                  | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.015 \text{ MHz} \leq f\_offset < 0.985 \text{ MHz}$               | -15 dBm             | 30 kHz                         |
| 10 MHz                 | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 0.95 \text{ MHz}$                 | -13 dBm             | 100 kHz                        |
| 15 MHz                 | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 0.95 \text{ MHz}$                 | -13 dBm             | 100 kHz                        |
| 20 MHz                 | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 0.95 \text{ MHz}$                 | -13 dBm             | 100 kHz                        |
| All                    | $1 \text{ MHz} \leq \Delta f < \Delta f_{max}$                | $1.05 \text{ MHz} \leq f\_offset < f\_offset_{max}$                  | -13 dBm             | 100 kHz                        |

In certain regions the following requirement may apply. For E-UTRA FDD repeaters operating in Bands 2, 4, 10, 23, and 25 emissions shall not exceed the maximum levels specified in Table 9.1.3-2.

**Table 9.1.3-2: Additional operating band unwanted emission limits for E-UTRA bands >1GHz**

| Input signal bandwidth | Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement | Measurement bandwidth (Note 1) |
|------------------------|---------------------------------------------------------------|----------------------------------------------------------------------|---------------------|--------------------------------|
| 1.4 MHz                | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.005 \text{ MHz} \leq f\_offset < 0.995 \text{ MHz}$               | -14 dBm             | 10 kHz                         |
| 3 MHz                  | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.015 \text{ MHz} \leq f\_offset < 0.985 \text{ MHz}$               | -13 dBm             | 30 kHz                         |
| 5 MHz                  | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.015 \text{ MHz} \leq f\_offset < 0.985 \text{ MHz}$               | -15 dBm             | 30 kHz                         |
| 10 MHz                 | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 0.95 \text{ MHz}$                 | -13 dBm             | 100 kHz                        |
| 15 MHz                 | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 0.95 \text{ MHz}$                 | -15 dBm             | 100 kHz                        |
| 20 MHz                 | $0 \text{ MHz} \leq \Delta f < 1 \text{ MHz}$                 | $0.05 \text{ MHz} \leq f\_offset < 0.95 \text{ MHz}$                 | -16 dBm             | 100 kHz                        |
| All                    | $1 \text{ MHz} \leq \Delta f < \Delta f_{max}$                | $1.5 \text{ MHz} \leq f\_offset < f\_offset_{max}$                   | -13 dBm             | 1 MHz                          |

In certain regions the following requirement may apply. For E-UTRA FDD repeaters operating in Bands 12, 13, 14 and 17 emissions shall not exceed the maximum levels specified in Table 9.1.3-3.

**Table 9.1.3-3: Additional operating band unwanted emission limits for E-UTRA (bands 12, 13, 14 and 17)**

| Input signal bandwidth | Frequency offset of measurement filter -3dB point, $\Delta f$ | Frequency offset of measurement filter centre frequency, $f\_offset$ | Minimum requirement | Measurement bandwidth (Note 1) |
|------------------------|---------------------------------------------------------------|----------------------------------------------------------------------|---------------------|--------------------------------|
| All                    | $0 \text{ MHz} \leq \Delta f < 100 \text{ kHz}$               | $0.015 \text{ MHz} \leq f\_offset < 0.085 \text{ MHz}$               | -13 dBm             | 30 kHz                         |
| All                    | $100 \text{ kHz} \leq \Delta f < \Delta f_{max}$              | $150 \text{ kHz} \leq f\_offset < f\_offset_{max}$                   | -13 dBm             | 100 kHz                        |

In certain regions the following requirement may apply for protection of DTT. For E-UTRA Repeater operating in Band 20, the level of emissions in the band 470-790 MHz, measured in an 8MHz filter bandwidth on centre frequencies  $F_{filter}$  according to Table 9.1.3-4, shall not exceed the maximum emission level  $P_{EM,N}$  declared by the manufacturer. This requirement applies in the frequency range 470-790 MHz even though part of the range falls in the spurious domain.

**Table 9.1.3-4: Declared emissions levels for protection of DTT**

| Filter centre frequency, $F_{filter}$                                 | Measurement bandwidth | Declared emission level [dBm] |
|-----------------------------------------------------------------------|-----------------------|-------------------------------|
| $F_{filter} = 8 \cdot N + 306 \text{ (MHz)}$ ;<br>$21 \leq N \leq 60$ | 8 MHz                 | $P_{EM,N}$                    |

This requirement may be applied for the protection in bands adjacent to bands 1, as defined in clause 5.5 in geographic areas in which both an adjacent band service and E-UTRA are deployed.

The requirement applies only to the down-link direction of the repeater.

The power of any spurious emission shall not exceed:

**Table 9.1.3-5 E-UTRA Repeater down-link spurious emissions limits for protection of adjacent band services**

| Operating Band | Band          | Maximum Level                                  | Measurement Bandwidth | Note |
|----------------|---------------|------------------------------------------------|-----------------------|------|
| I              | 2100-2105 MHz | $-30 + 3.4 (f - 2100 \text{ MHz}) \text{ dBm}$ | 1 MHz                 |      |
|                | 2175-2180 MHz | $-30 + 3.4 (2180 \text{ MHz} - f) \text{ dBm}$ | 1 MHz                 |      |

Note: The regional requirement is defined in terms of EIRP (effective isotropic radiated power), which is dependent on both the repeater emissions at the antenna connector and the deployment (including antenna gain and feeder loss). The requirement defined above provides the characteristics of the repeater needed to verify compliance with the regional requirement. Compliance with the regional requirement can be determined using the method outlined in TS.36.104 [6] Annex G.

NOTE 1: As a general rule for the requirements in Clause 9.1.3, the resolution bandwidth of the measuring equipment should be equal to the measurement bandwidth. However, to improve measurement accuracy, sensitivity and efficiency, the resolution bandwidth may be smaller than the measurement bandwidth. When the resolution bandwidth is smaller than the measurement bandwidth, the result should be integrated over the measurement bandwidth in order to obtain the equivalent noise bandwidth of the measurement bandwidth.

NOTE 2: For signal bandwidths between the values given in Table's 9.1.3-1 and 9.1.3-2, the requirements can be calculated by linearly interpolating between the requirements closest to the wanted signal bandwidth.

In regions where FCC regulation applies, requirements for protection of GPS according to FCC Order DA 10-534 applies for operation in Band 24. The following normative requirement covers the Repeater to be used together with other information about the site installation to verify compliance with the requirement in FCC Order DA 10-534. The requirement applies to repeater operating in Band 24 to ensure that appropriate interference protection is provided to the 1559 – 1610 MHz band. This requirement applies to the frequency range 1559-1610 MHz even though part of this range falls within the operating band unwanted emissions domain.

The level of emissions in the 1559 – 1610 MHz band, measured in measurement bandwidth according to Table 6.6.4.3.1-4 shall not exceed the maximum emission levels  $P_{E\_1\text{MHz}}$  and  $P_{E\_1\text{kHz}}$  declared by the manufacturer.

**Table 9.1.3-5A: Declared emissions levels for protection of the 1559-1610 MHz band**

| Operating Band | Frequency range | Declared emission level [dBW]<br>(Measurement bandwidth = 1 MHz) | Declared emission level [dBW] of discrete emissions of less than 700 Hz bandwidth<br>(Measurement bandwidth = 1 kHz) |
|----------------|-----------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 24             | 1559 - 1610 MHz | $P_{E\_1\text{MHz}}$                                             | $P_{E\_1\text{kHz}}$                                                                                                 |

Note: The regional requirement in FCC Order DA 10-534 is defined in terms of EIRP (effective isotropic radiated power), which is dependent on both the repeater emissions at the antenna connector and the deployment (including antenna gain and feeder loss). The EIRP level is calculated using:  $P_{\text{EIRP}} = P_E + G_{\text{ant}}$  where  $P_E$  denotes the Repeater unwanted emission level at the antenna connector,  $G_{\text{ant}}$  equals the Repeater antenna gain minus feeder loss. The requirement defined above provides the characteristics of the Repeater needed to verify compliance with the regional requirement.

### 9.1.4. Protection of the BS receiver in the operating band

This requirement shall be applied for the protection of E-UTRA FDD BS receiver in geographic areas in which E-UTRA-FDD Repeater and E-UTRA-FDD BS are deployed.

The requirement applies at frequencies that are more than 10 MHz below or more than 10 MHz above the repeater pass band.

#### 9.1.4.1 Minimum Requirement

This requirement applies to the uplink of the repeater, at maximum gain.

The power of any operating band unwanted emission shall not exceed the limits in Table 9.1.4.1-1.

**Table 9.1.4.1-1: Uplink operating band unwanted emissions limits for protection of the BS receiver**

| Maximum Level | Measurement Bandwidth | Note |
|---------------|-----------------------|------|
| -53 dBm       | 100 kHz               |      |

NOTE 1: These requirements in Table 9.1.4.1-1: for the uplink direction of the Repeater reflect what can be achieved with present state of the art technology and are based on a coupling loss of 73 dB between a Repeater and an E-UTRA FDD BS receiver.

NOTE 2: The requirements shall be reconsidered when the state of the art technology progresses.

NOTE 3: The protection of R-GSM is for further study.

## 9.2 Spurious emissions

The spurious emission limits apply from 9 kHz to 12.75 GHz, (or above, as indicated in Table 9.2.1.1.1-1 and 9.2.1.2.1-1), excluding the frequency range from 10 MHz below the lowest frequency of the repeaters operating band up to 10 MHz above the highest frequency of the repeaters operating band. Exceptions are the requirement in Table 9.2.2.1-2 and 9.2.2.1-3 that apply also closer than 10 MHz from repeaters operating band.

The requirements shall apply whatever the type of repeater considered (one or several pass bands). It applies for all configurations foreseen by the manufacturer's specification.

Unless otherwise stated, all requirements are measured as mean power (RMS).

### 9.2.1 Mandatory requirements

The requirements of either subclause 9.2.1.1 (Category A limits) or subclause 9.2.1.2 (Category B limits) shall apply. The application of either Category A or Category B limits shall be the same as for Operating band unwanted emissions in subclause 9.1.

The requirements of either subclause 9.2.1.1 or subclause 9.2.1.2 apply to the uplink and downlink of the repeater, at maximum gain, and with the following input signals:

- without E-UTRA input signal
- with E-UTRA input signals in the pass band of the repeater, at levels that produce the maximum rated power output per channel
- with 10 dB increased E-UTRA input signals in all channels in the pass band, compared to the input level producing the maximum rated output power.

#### 9.2.1.1 Spurious emissions (Category A)

##### 9.2.1.1.1 Minimum Requirement

The power of any spurious emission shall not exceed the limits in Table 9.2.1.1.1-1.

**Table 9.2.1.1.1-1: Spurious emission limits, Category A**

| Frequency range                                                                                                                               | Maximum level | Measurement Bandwidth | Note           |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------|----------------|
| 9kHz - 150kHz                                                                                                                                 | -13 dBm       | 1 kHz                 | Note 1         |
| 150kHz - 30MHz                                                                                                                                |               | 10 kHz                | Note 1         |
| 30MHz - 1GHz                                                                                                                                  |               | 100 kHz               | Note 1         |
| 1GHz - 12.75 GHz                                                                                                                              |               | 1 MHz                 | Note 2         |
| 12.75 GHz – 5 <sup>th</sup> harmonic of the upper frequency edge of the DL or UL operating band for DL or UL spurious emissions, respectively |               | 1 MHz                 | Note 2, Note 3 |

NOTE 1: Bandwidth as in ITU-R SM.329 [2], s4.1  
NOTE 2: Bandwidth as in ITU-R SM.329 [2], s4.1. Upper frequency as in ITU-R SM.329 [2], s2.5 table 1  
NOTE 3: Applies only for Bands 22.

#### 9.2.1.2 Spurious emissions (Category B)

##### 9.2.1.2.1 Minimum Requirement

The power of any spurious emission shall not exceed the limits in Table 9.2.1.2.1-1.

**Table 9.2.1.2.1-1: Spurious emissions limits, Category B**

| Frequency range                                                                                                                               | Maximum Level | Measurement Bandwidth | Note           |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------|----------------|
| 9 kHz ↔ 150 kHz                                                                                                                               | -36 dBm       | 1 kHz                 | Note 1         |
| 150 kHz ↔ 30 MHz                                                                                                                              | -36 dBm       | 10 kHz                | Note 1         |
| 30 MHz ↔ 1 GHz                                                                                                                                | -36 dBm       | 100 kHz               | Note 1         |
| 1 GHz ↔ 12.75 GHz                                                                                                                             | -30 dBm       | 1 MHz                 | Note 2         |
| 12.75 GHz – 5 <sup>th</sup> harmonic of the upper frequency edge of the DL or UL operating band for DL or UL spurious emissions, respectively | -30 dBm       | 1 MHz                 | Note 2, Note 3 |

NOTE 1: Bandwidth as in ITU-R SM.329 [2], s4.1  
NOTE 2: Bandwidth as in ITU-R SM.329 [2], s4.1. Upper frequency as in ITU-R SM.329 [2], s2.5 table 1  
NOTE 3: Applies only for Bands 22.

### 9.2.2 Co-existence with other systems in the same geographical area

These requirements may be applied for the protection of system operating in frequency ranges other than the E-UTRA Repeater operating band. The limits may apply as an optional protection of such systems that are deployed in the same geographical area as the E-UTRA Repeater, or they may be set by local or regional regulation as a mandatory requirement for an E-UTRA operating band. It is in some cases not stated in the present document whether a requirement is mandatory or under what exact circumstances that a limit applies, since this is set by local or regional regulation. An overview of regional requirements in the present document is given in Clause 4.2.

Some requirements may apply for the protection of specific equipment (UE, MS and/or BS) or equipment operating in specific systems (GSM, UTRA, E-UTRA, etc.) as listed below.

#### 9.2.2.1 Minimum requirement

Unless otherwise stated this requirement applies to the uplink and downlink of the repeater, at maximum gain.

The power of any spurious emission shall not exceed the limits of Table 9.2.2.1-1 for an E-UTRA Repeater where requirements for co-existence with the system listed in the first column apply.

**Table 9.2.2.1-1: Spurious emissions limits for E-UTRA-FDD repeater in geographic coverage area of systems operating in other frequency bands**

| System type operating in the same geographical area | Frequency range for co-existence requirement | Maximum Level | Measurement Bandwidth | Note                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------|---------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GSM900                                              | 921 - 960 MHz                                | -57 dBm       | 100 kHz               | This requirement does not apply to E-UTRA FDD Repeater operating in band 8.                                                                                                                                                                                                                                                                                                     |
|                                                     | 876 - 915 MHz                                | -61 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                   |
| DCS1800                                             | 1805 - 1880 MHz                              | -47 dBm       | 100 kHz               | This requirement does not apply to E-UTRA FDD Repeater operating in band 3.                                                                                                                                                                                                                                                                                                     |
|                                                     | 1710 - 1785 MHz                              | -61 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 3, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                   |
| PCS1900                                             | 1930 - 1990 MHz                              | -47 dBm       | 100 kHz               | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                                                                                                                                                                                                                          |
|                                                     | 1850 - 1910 MHz                              | -61 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                        |
| GSM850 or CDMA850                                   | 869 - 894 MHz                                | -57 dBm       | 100 kHz               | This requirement does not apply to E-UTRA FDD Repeater operating in band 5.                                                                                                                                                                                                                                                                                                     |
|                                                     | 824 - 849 MHz                                | -61 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                   |
| UTRA FDD Band I or E-UTRA Band 1                    | 2110 - 2170 MHz                              | -52 dBm       | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 1.                                                                                                                                                                                                                                                                                                     |
|                                                     | 1920 - 1980 MHz                              | -49 dBm       | 1 MHz                 | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                   |
| UTRA FDD Band II or E-UTRA Band 2                   | 1930 - 1990 MHz                              | -52 dBm       | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                                                                                                                                                                                                                          |
|                                                     | 1850 - 1910 MHz                              | -49 dBm       | 1 MHz                 | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                        |
| UTRA FDD Band III or E-UTRA Band 3                  | 1805 - 1880 MHz                              | -52 dBm       | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 3 or band 9.                                                                                                                                                                                                                                                                                           |
|                                                     | 1710 - 1785 MHz                              | -49 dBm       | 1 MHz                 | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 3, since it is already covered by the requirement in sub-clause 9.1.4.<br>This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 9 in the frequency Range from 1749,9 MHz to 1784,9 MHz, since it is already covered by the requirement in clause 9.1.4. |
| UTRA FDD Band IV or E-UTRA Band 4                   | 2110 - 2155 MHz                              | -52 dBm       | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 4 or band 10.                                                                                                                                                                                                                                                                                          |
|                                                     | 1710 - 1755 MHz                              | -49 dBm       | 1 MHz                 | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 4 or band 10, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                        |
| UTRA FDD Band V or E-UTRA Band 5                    | 869 - 894 MHz                                | -52 dBm       | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 5.                                                                                                                                                                                                                                                                                                     |
|                                                     | 824 - 849 MHz                                | -49 dBm       | 1 MHz                 | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                   |
|                                                     | 860 - 890 MHz                                | -52 dBm       | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 5, 6, 18, 19 or 20.                                                                                                                                                                                                                                                                                    |

|                                                 |                     |         |       |                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------|---------------------|---------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UTRA FDD Band VI, XIX or E-UTRA Band 6, 18, 19  | 815 – 830 MHz       | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 18, since it is already covered by the requirement in sub-clause 9.1.4. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, 6, 19 or 20.                                                                                                        |
|                                                 | 830 – 845 MHz       | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 619, since it is already covered by the requirement in sub-clause 9.1.4. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, 18 or 20.                                                                                                          |
| UTRA FDD Band VII or E-UTRA Band 7              | 2620 - 2690 MHz     | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                                                                                                                                  |
|                                                 | 2500 - 2570 MHz     | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 7, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                |
| UTRA FDD Band VIII or E-UTRA Band 8             | 925 – 960 MHz       | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 8.                                                                                                                                                                                                                                                                                                  |
|                                                 | 880 – 915 MHz       | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                                |
| UTRA FDD Band IX or E-UTRA Band 9               | 1844.9 - 1879.9 MHz | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 3 or band 9.                                                                                                                                                                                                                                                                                        |
|                                                 | 1749.9 - 1784.9 MHz | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 3 or band 9, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                      |
| UTRA FDD Band X or E-UTRA Band 10               | 2110 - 2170 MHz     | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 4 or band 10                                                                                                                                                                                                                                                                                        |
|                                                 | 1710 - 1770 MHz     | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 10, since it is already covered by the requirement in sub-clause 9.1.4.<br>This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 4 in the frequency Range from 1710 MHz to 1755 MHz, since it is already covered by the requirement in clause 9.1.4. |
| UTRA FDD Band XI or XXI or E-UTRA Band 11 or 21 | 1475.9 - 1510.9 MHz | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 11 or 21                                                                                                                                                                                                                                                                                            |
|                                                 | 1427.9 - 1447.9 MHz | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 11, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                               |
|                                                 | 1447.9 - 1462.9 MHz | -49 dBm | 1MHz  | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 21, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                               |
| UTRA FDD Band XII or E-UTRA Band 12             | 728 - 746 MHz       | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 12.                                                                                                                                                                                                                                                                                                 |
|                                                 | 698 - 716 MHz       | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 12, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                               |
| UTRA FDD Band XIII or E-UTRA Band 13            | 746 - 756 MHz       | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 13.                                                                                                                                                                                                                                                                                                 |
|                                                 | 777 - 787 MHz       | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 13, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                               |
| UTRA FDD Band XIV or E-UTRA Band 14             | 758 - 768 MHz       | -52 dBm | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 14.                                                                                                                                                                                                                                                                                                 |
|                                                 | 788 - 798 MHz       | -49 dBm | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 14, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                                                                                               |

|                                       |                     |         |         |                                                                                                                                                                                                                                                                                               |
|---------------------------------------|---------------------|---------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E-UTRA Band 17                        | 734 – 746 MHz       | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 17.                                                                                                                                                                                                                  |
|                                       | 704 - 716 MHz       | -49 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 17, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                |
| UTRA FDD Band XX or E-UTRA Band 20    | 791 – 821 MHz       | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 20.                                                                                                                                                                                                                  |
|                                       | 832 - 862 MHz       | -49 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 20, since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                |
| UTRA FDD Band XXII or E-UTRA Band 22  | 3510-3590 MHz       | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 22.                                                                                                                                                                                                                  |
|                                       | 3410 – 3490 MHz     | -49 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 22 since it is already covered by the requirement in sub-clause 9.1.4.                                                                                                                                 |
| E-UTRA Band 23                        | 2180 – 2200 MHz     | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 23.                                                                                                                                                                                                                  |
|                                       | 2000 - 2020 MHz     | -49 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 23 since it is already covered by the requirement in sub-clause 9.1.4. This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25, where the limits are defined separately. |
|                                       | 2000 – 2010 MHz     | -30 dBm | 1 MHz   | This requirement only applies to the uplink E-UTRA FDD Repeater operating in band 2 or band 25. This requirement applies starting 5 MHz above the band 25 downlink operating band.                                                                                                            |
|                                       | 2010 – 2020 MHz     | -49 dBm | 1 MHz   |                                                                                                                                                                                                                                                                                               |
| E-UTRA Band 24                        | 1525 – 1559 MHz     | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA Repeaters operating in band 24.                                                                                                                                                                                                                     |
|                                       | 1626.5 – 1660.5 MHz | -49 dBm | 1 MHz   | This requirement does not apply to E-UTRA Repeater operating in band 24, since it is already covered by the requirement in subclause 9.1.4.                                                                                                                                                   |
| UTRA FDD Band XXV or E-UTRA Band 25   | 1930 – 1995 MHz     | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                                                                                                                                        |
|                                       | 1850 – 1915 MHz     | -49 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 25 since it is already covered by the requirement in sub-clause 9.1.4. For E-UTRA FDD Repeater operating in band 2, it applies for 1910 MHz to 1915 MHz, while the rest is covered in sub-clause 9.1.4 |
| UTRA TDD in Band a) or E-UTRA Band 33 | 1900 - 1920 MHz     | -52 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                                  |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                                 |
| UTRA TDD in Band a) or E-UTRA Band 34 | 2010 - 2025 MHz     | -52 dBm | 1 MHz   |                                                                                                                                                                                                                                                                                               |
| UTRA TDD in Band b) or E-UTRA Band 35 | 1850 – 1910 MHz     | -52 dBm | 1 MHz   | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 3 or band 9. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                    |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                                                                                                                         |
| UTRA TDD in Band b) or E-UTRA Band 36 | 1930 - 1990 MHz     | -52 dBm | 1 MHz   | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 2 or band 25. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                                              |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                                                                                                                                                    |

|                                       |                 |         |         |                                                                                                                                                                                                                                                                             |
|---------------------------------------|-----------------|---------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UTRA TDD in Band c) or E-UTRA Band 37 | 1910 - 1930 MHz | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25.<br>This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.<br>This unpaired band is defined in ITU-R M.1036, but is pending any future deployment. |
|                                       |                 | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                               |
| UTRA TDD in Band d) or E-UTRA Band 38 | 2570 – 2620 MHz | -52 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                   |
|                                       |                 | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                  |
| UTRA TDD Band f) or E-UTRA Band 39    | 1880 – 1920 MHz | -52 dBm | 1 MHz   | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                |
|                                       |                 | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                               |
| UTRA TDD Band e) or E-UTRA Band 40    | 2300 – 2400 MHz | -52 dBm | 1 MHz   |                                                                                                                                                                                                                                                                             |
| E-UTRA Band 41                        | 2496 – 2690 MHz | -52 dBm | 1 MHz   |                                                                                                                                                                                                                                                                             |
| E-UTRA Band 42                        | 3400 – 3600 MHz | -52 dBm | 1 MHz   | This requirement does not apply to E-UTRA FDD Repeater operating in band 22.                                                                                                                                                                                                |
| E-UTRA Band 43                        | 3600 – 3800 MHz | -52 dBm | 1 MHz   |                                                                                                                                                                                                                                                                             |
|                                       |                 | -53 dBm | 100 kHz |                                                                                                                                                                                                                                                                             |

NOTE 1: As defined in the scope for spurious emissions in this clause, the co-existence requirements in Table 9.2.2.1-1 do not apply for the 10 MHz frequency range immediately outside the repeaters operating band frequency range of an operating band (see Table 5.5-1). This is also the case when the repeaters operating band frequency range is adjacent to the band for the co-existence requirement in the Table 9.2.2.1-1. Emission limits for this excluded frequency range may also be covered by local or regional requirements.

NOTE 2: The Table 9.2.2.1-1 assumes that two operating bands, where the frequency ranges in Table 5.5-1 would be overlapping, are not deployed in the same geographical area. For such a case of operation with overlapping frequency arrangements in the same geographical area, special co-existence requirements may apply that are not covered by the 3GPP specifications.

NOTE 3: The requirements of -53dBm/100kHz in Table 9.2.2.1-1 for the up link direction of the Repeater reflect what can be achieved with present state of the art technology and are based on a coupling loss of 73 dB between a Repeater and a UTRA TDD BS receiver.

NOTE 4: The requirements of -53dBm/100kHz in Table 9.2.2.1-1 shall be reconsidered when the state of the art technology progresses.

The following requirement may be applied for the protection of PHS in geographic areas in which both PHS and E-UTRA-FDD repeaters are deployed. This requirement is also applicable at specified frequencies falling between 10 MHz below the lowest frequency of the repeaters operating band and 10 MHz above the highest frequency of the repeaters operating band.

Unless otherwise stated this requirement applies to the uplink and downlink of the repeater, at maximum gain.

The power of any spurious emission shall not exceed:

**Table 9.2.2.1-2: Spurious emissions limits for E-UTRA-FDD repeater in geographic coverage area of PHS**

| Frequency range     | Maximum Level | Measurement Bandwidth | Note                                                                        |
|---------------------|---------------|-----------------------|-----------------------------------------------------------------------------|
| 1884.5 - 1915.7 MHz | -41 dBm       | 300 kHz               | Applicable when co-existence with PHS system operating in 1884.5 -1915.7MHz |

The following requirement shall be applied to E-UTRA-FDD repeaters operating in Bands 13 and 14 to ensure that appropriate interference protection is provided to 700 MHz public safety operations. This requirement is also applicable at specified frequencies falling between 10 MHz below the lowest frequency of the repeaters operating band and 10 MHz above the highest frequency of the repeaters operating band

Unless otherwise stated this requirement applies to the uplink and downlink of the repeater, at maximum gain.

The power of any spurious emission shall not exceed:

**Table 9.2.2.1-3: Spurious emissions limits for E-UTRA-FDD repeater for protection of public safety operations**

| Operating Band | Frequency range | Maximum Level | Measurement Bandwidth | Note |
|----------------|-----------------|---------------|-----------------------|------|
| 13             | 763 - 775 MHz   | -46 dBm       | 6.25 kHz              |      |
| 13             | 793 - 805 MHz   | -46 dBm       | 6.25 kHz              |      |
| 14             | 769 - 775 MHz   | -46 dBm       | 6.25 kHz              |      |
| 14             | 799 - 805 MHz   | -46 dBm       | 6.25 kHz              |      |

### 9.2.3 Co-location with base stations

These requirements may be applied for the protection of other BS receivers when GSM900, DCS1800, PCS1900, GSM850 UTRA FDD, UTRA TDD and/or E-UTRA BS are co-located with an E-UTRA FDD Repeater.

Unless otherwise stated the requirements assume a 30 dB coupling loss between transmitter and receiver.

NOTE: For co-location with UTRA, the requirements are based on co-location with Wide Area UTRA FDD or TDD base stations.

#### 9.2.3.1 Minimum Requirements

Unless otherwise stated this requirement applies to the uplink and downlink of the repeater, at maximum gain.

The power of any spurious emission shall not exceed the limits of Table 9.2.3.1-1 for an E-UTRA FDD Repeater where requirements for co-location with a Base Station listed in the first column apply.

**Table 9.2.3.1-1: Spurious emissions limits for E-UTRA-FDD Repeater co-located with Base Stations**

| Type of co-located Base Station                    | Frequency range for co-location requirement | Maximum Level | Measurement Bandwidth | Note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------|---------------------------------------------|---------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GSM900                                             | 876 - 915 MHz                               | -98 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 75dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                          |
| DCS1800                                            | 1710 - 1785 MHz                             | -98 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 3, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 75dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                          |
| PCS1900                                            | 1850 - 1910 MHz                             | -98 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 75dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                               |
| GSM850 or CDMA850                                  | 824 - 849 MHz                               | -98 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 75dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                          |
| UTRA FDD Band I or E-UTRA Band 1                   | 1920 - 1980 MHz                             | -96 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                          |
| UTRA FDD Band II or E-UTRA Band 2                  | 1850 - 1910 MHz                             | -96 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                               |
| UTRA FDD Band III or E-UTRA Band 3                 | 1710 - 1785 MHz                             | -96 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 3, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 9 in the frequency Range from 1749,9 MHz to 1784,9 MHz, since it is already covered by the requirement in clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. |
| UTRA FDD Band IV or E-UTRA Band 4                  | 1710 - 1755 MHz                             | -96 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 4 or band 10, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                               |
| UTRA FDD Band V or E-UTRA Band 5                   | 824 - 849 MHz                               | -96 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                          |
| UTRA FDD Band VI or XIX or E-UTRA Band 6, 18 or 19 | 815 - 830 MHz                               | -96 dBm       | 100 kHz               | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 18, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, 6, 19 or 20.                                                                                                                                                                                                  |

|                                                 |                     |         |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------|---------------------|---------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                 | 830 - 845 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 6 or 19, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, 18 or 20.                                                                                                                                                                                             |
| UTRA FDD Band VII or E-UTRA Band 7              | 2500 - 2570 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 7, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                       |
| UTRA FDD Band VIII or E-UTRA Band 8             | 880 - 915 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                       |
| UTRA FDD Band IX or E-UTRA Band 9               | 1749.9 - 1784.9 MHz | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 3 or band 9, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                             |
| UTRA FDD Band X or E-UTRA Band 10               | 1710 - 1770 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 10, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 4 in the frequency Range from 1710 MHz to 1755 MHz, since it is already covered by the requirement in clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. |
| UTRA FDD Band XI or XXI or E-UTRA Band 11 or 21 | 1427.9 - 1447.9 MHz | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 11, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                      |
|                                                 | 1447.9 - 1462.9 MHz | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 21, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                      |
| UTRA FDD Band XII or E-UTRA Band 12             | 698 - 716 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 12, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                      |
| UTRA FDD Band XIII or E-UTRA Band 13            | 777 - 787 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 13, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                      |
| UTRA FDD Band XIV or E-UTRA Band 14             | 788 - 798 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 14, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                      |
| E-UTRA Band 17                                  | 704 - 716 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 17, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                                                                                      |

|                                       |                     |         |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|---------------------|---------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UTRA FDD Band XX or E-UTRA Band 20    | 832 - 862 MHz       | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 20, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                          |
| UTRA FDD Band XXII or E-UTRA Band 22  | 3410 - 3490 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 22, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                          |
| E-UTRA Band 23                        | 2000 - 2020 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 23, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                          |
| E-UTRA Band 24                        | 1626.5 – 1660.5 MHz | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 24, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port.                                                                                                                                                                                                                                          |
| UTRA FDD Band XXV or E-UTRA Band 25   | 1850 - 1915 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 25, since it is already covered by the requirement in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. For the uplink of E-UTRA FDD Repeater operating in band 2, it applies for 1910 MHz to 1915 MHz, while the rest is covered in sub-clause 9.1.4, but requires a 73dB coupling loss between base station and the repeater UL transmit port. |
| UTRA TDD in Band a) or E-UTRA Band 33 | 1900 - 1920 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                                                                                                                                                                                                                                      |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                                                                                                                                                                                                                                     |
| UTRA TDD in Band a) or E-UTRA Band 34 | 2010 - 2025 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                       |                     | -83 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                                                                                                                                                                                                                                                                                                                                                        |
| UTRA TDD in Band b) or E-UTRA Band 35 | 1850 – 1910 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 3 or band 9. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                                                                                                                                                                                                                        |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25.                                                                                                                                                                                                                                                                                                                                                                                             |
| UTRA TDD in Band b) or E-UTRA Band 36 | 1930 – 1990 MHz     | -96 dBm | 100 kHz | This is not applicable to the downlink of E-UTRA-FDD Repeater operating in band 2 or band 25. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                                                                                                                                                                                                                                                           |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                                                                                                                                                                                                                                                                                                                                                        |
| UTRA TDD in Band c) or E-UTRA Band 37 | 1910 - 1930 MHz     | -96 dBm | 100 kHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1. This unpaired band is defined in ITU-R M.1036, but is pending any future deployment.                                                                                                                                                                                                                             |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                                                                                                                                                                                                                                     |
| UTRA TDD in Band d) or E-UTRA Band 38 | 2570 – 2620 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                       |                     | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                                                                                                                                                                                                                                        |
| UTRA TDD Band f) or E-UTRA Band 39    | 1880 – 1920 MHz     | -96 dBm | 100 kHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                                                                                                                                                                                                                                      |

|                                    |                 |         |         |                                                                                                               |
|------------------------------------|-----------------|---------|---------|---------------------------------------------------------------------------------------------------------------|
|                                    |                 | -53 dBm | 100 kHz | This requirement is applied only to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25. |
| UTRA TDD Band e) or E-UTRA Band 40 | 2300 – 2400 MHz | -96 dBm | 100 kHz |                                                                                                               |
| E-UTRA Band 41                     | 2496 – 2690 MHz | -96 dBm | 100 kHz |                                                                                                               |
| E-UTRA Band 42                     | 3400 – 3600 MHz | -96 dBm | 100 kHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 22.                                  |
| E-UTRA Band 43                     | 3600 – 3800 MHz | -96 dBm | 100 kHz |                                                                                                               |
|                                    |                 | -53 dBm | 100 kHz |                                                                                                               |

NOTE 1: As defined in the scope for spurious emissions in this clause, the co-location requirements in Table 9.2.3.1-1 do not apply for the 10 MHz frequency range immediately outside the repeaters operating band frequency range of an operating band (see Table 5.5-1). This is also the case when the repeaters operating band frequency range is adjacent to the frequency range of the co-location requirement in the Table 9.2.3.1-1. The current state-of-the-art technology does not allow a single generic solution for co-location with other system on adjacent frequencies for 30dB Repeater-BS minimum coupling loss. However, there are certain site-engineering solutions that can be used. These techniques are addressed in TR 25.942 [5].

NOTE 2: The Table 9.2.3.1-1 assumes that two operating bands, where the corresponding eNode B transmit and receive frequency ranges in Table 5.5-1 would be overlapping, are not deployed in the same geographical area. For such a case of operation with overlapping frequency arrangements in the same geographical area, special co-location requirements may apply that are not covered by the 3GPP specifications.

NOTE 3: The requirements of -53dBm/100kHz in Table 9.2.3.1-1 for the up link direction of the Repeater reflect what can be achieved with present state of the art technology and are based on a coupling loss of 73 dB between a Repeater and a UTRA TDD BS receiver.

NOTE 4: The requirements of -83dBm/100kHz in Table 9.2.3.1-1 for the up link direction of the Repeater reflect what can be achieved with present state of the art technology and are based on a coupling loss of 43 dB between a Repeater and a UTRA TDD BS receiver.

NOTE 5: The requirements of -53dBm/100kHz and -83dBm/100kHz in Table 9.2.3.1-1 shall be reconsidered when the state of the art technology progresses.

# 10 Error Vector Magnitude

## 10.1 Downlink Error Vector Magnitude

The Error Vector Magnitude is a measure of the difference between the ideal symbols and the measured symbols after the equalization. This difference is called the error vector. The equaliser parameters are estimated as defined in TS36.104 [6] Annex E. The EVM result is defined as the square root of the ratio of the mean error vector power to the mean reference power expressed in percent.

### 10.1.1 Minimum requirement

For all E-UTRA channel bandwidths, as defined in sub-clause 5.6, applicable to the repeater, the EVM measurement shall be performed over all allocated resource blocks and subframes within a frame. The EVM value is then calculated as the mean square root of the measured values.

For the downlink of the repeater the Error Vector Magnitude shall not be worse than 8 %.

## 10.2 Uplink Error Vector Magnitude

The Error Vector Magnitude is a measure of the difference between the reference waveform and the measured waveform. This difference is called the error vector. Before calculating the EVM the measured waveform is corrected by the sample timing offset and RF frequency offset. Then the IQ origin offset shall be removed from the measured waveform before calculating the EVM.

The measured waveform is further modified by selecting the absolute phase and absolute amplitude of the Tx chain. The EVM result is defined after the front-end IDFT as the square root of the ratio of the mean error vector power to the mean reference power expressed as a %. The basic EVM measurement interval is one slot in the time domain.

### 10.2.1 Minimum requirement

For the uplink of the repeater the RMS average of the basic EVM measurements for 10 consecutive sub-frames for the different modulations schemes shall not exceed 8 %.

# 11 Input Intermodulation

The input intermodulation is a measure of the capability of the repeater to inhibit the generation of interference in the pass band, in the presence of interfering signals on frequencies other than the pass band.

## 11.1 General requirement

The following requirement applies for interfering signals in the operating bands defined in sub-clause 5.5, depending on the repeaters pass band.

This requirement applies to the uplink and downlink of the repeater, at maximum gain.

### 11.1.1 Minimum requirement

For the parameters specified in table 11.1.1-1, the power in the pass band shall not increase with more than 10 dB at the output of the repeater as measured in the centre of the pass band, compared to the level obtained without interfering signals applied.

The frequency separation between the two interfering signals shall be adjusted so that the 3<sup>rd</sup> order intermodulation product is positioned in the centre of the pass band.

Table 11.1.1-1 specifies the parameters for two interfering signals, where:

- $f_1$  offset is the offset from the channel edge frequency of the first or last channel in the pass band of the closer carrier.

**Table 11.1.1-1: Input intermodulation requirement**

| $f_1$ offset | Interfering Signal Levels | Type of signals | Measurement bandwidth |
|--------------|---------------------------|-----------------|-----------------------|
| 1,0 MHz      | -40 dBm                   | 2 CW carriers   | 1 MHz                 |

## 11.2 Co-location with BS in other systems

This additional input intermodulation requirement may be applied for the protection of E-UTRA FDD Repeater input when GSM900, DCS1800, PCS1900, GSM850, UTRA FDD, UTRA TDD and/or E-UTRA BS are co-located with an E-UTRA FDD Repeater.

Unless otherwise stated this requirement applies to the uplink and downlink of the repeater, at maximum gain.

### 11.2.1 Minimum requirement

For the parameters specified in table 11.2.1-1, the power in the pass band shall not increase with more than 10 dB at the output of the repeater as measured in the centre of the pass band, compared to the level obtained without interfering signals applied.

The frequency separation between the two interfering signals shall be adjusted so that the lowest order intermodulation product is positioned in the centre of the pass band.

NOTE 1: The lowest intermodulation products correspond to the 4<sup>th</sup> and 3<sup>rd</sup> order for the GSM 900 and DCS 1800 bands, respectively.

#### **Table 11.2.1-1: Input intermodulation requirements for interfering signals in co-located other systems**

| Co-located other systems                      | Frequency of interfering signals | Interfering Signal Levels | Type of signals | Measurement bandwidth | Note                                                                                                                                                                                                                                               |
|-----------------------------------------------|----------------------------------|---------------------------|-----------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GSM900                                        | 921 - 960 MHz                    | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| DCS1800                                       | 1805 - 1880 MHz                  | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 3, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| PCS1900                                       | 1930 - 1990 MHz                  | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port. |
| GSM850 or CDMA850                             | 869 - 894 MHz                    | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA-FDD Band I or E-UTRA Band 1              | 2110 - 2170 MHz                  | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 1, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA-FDD Band II or E-UTRA Band 2             | 1930 - 1990 MHz                  | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port. |
| UTRA-FDD Band III or E-UTRA Band 3            | 1805 - 1880 MHz                  | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 3 or band 9, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.  |
| UTRA-FDD Band IV or E-UTRA Band 4             | 2110 - 2155 MHz                  | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 4 or band 10, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port. |
| UTRA-FDD Band V or E-UTRA Band 5              | 869 - 894 MHz                    | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA-FDD Band VI,XIX or E-UTRA Band 6, 18, 19 | 860 - 890 MHz                    | +16 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 6, 18 or 19 since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.   |

|                                                 |                     |         |               |       |                                                                                                                                                                                                                                                     |
|-------------------------------------------------|---------------------|---------|---------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UTRA-FDD Band VII or E-UTRA Band 7              | 2620 - 2690 MHz     | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 7, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.             |
| UTRA-FDD Band VIII or E-UTRA Band 8             | 925 - 960 MHz       | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.             |
| UTRA-FDD Band IX or E-UTRA Band 9               | 1844.9 - 1879.9 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 3 or band 9, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.   |
| UTRA-FDD Band X or E-UTRA Band 10               | 2110 - 2170 MHz     | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 4 or band 10, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.  |
| UTRA-FDD Band XI or XXI or E-UTRA Band 11 or 21 | 1475.9 - 1510.9 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 11 or band 21, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port. |
| UTRA FDD Band XII or E-UTRA Band 12             | 728 - 746 MHz       | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 12, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA FDD Band XIII or E-UTRA Band 13            | 746 - 756 MHz       | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 13, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA FDD Band XIV or E-UTRA Band 14             | 758 - 768 MHz       | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 14, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| E-UTRA Band 17                                  | 734 - 746 MHz       | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 17, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA FDD Band XX or E-UTRA Band 20              | 791 - 821 MHz       | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 20, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |
| UTRA Band XXII or E-UTRA Band 22                | 3510 - 3590 MHz     | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 22, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.            |

|                                       |                 |         |               |       |                                                                                                                                                                                                                                                                             |
|---------------------------------------|-----------------|---------|---------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E-UTRA Band 23                        | 2180 – 2200 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 23, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.                                    |
| E-UTRA Band 24                        | 1525 - 1559 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 24, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.                                    |
| UTRA FDD Band XXV or E-UTRA Band 25   | 1930 – 1995 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 11.1, but requires a 86dB coupling loss between base station and the repeater DL receive port.                          |
| UTRA TDD in Band a) or E-UTRA Band 33 | 1900 - 1920 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                |
| UTRA TDD in Band a) or E-UTRA Band 34 | 2010 - 2025 MHz | +16 dBm | 2 CW carriers | 1 MHz |                                                                                                                                                                                                                                                                             |
| UTRA TDD in Band b) or E-UTRA Band 35 | 1850 – 1910 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 3 or band 9.<br>This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25.                                                               |
| UTRA TDD in Band b) or E-UTRA Band 36 | 1930 – 1990 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 2 or band 25.<br>This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                         |
| UTRA TDD in Band c) or E-UTRA Band 37 | 1910 - 1930 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25.<br>This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.<br>This unpaired band is defined in ITU-R M.1036, but is pending any future deployment. |
| UTRA TDD in Band d) or E-UTRA Band 38 | 2570 – 2620 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                   |
| UTRA TDD Band f) or E-UTRA Band 39    | 1880 – 1920 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                              |
| UTRA TDD Band e) or E-UTRA Band 40    | 2300 – 2400 MHz | +16 dBm | 2 CW carriers | 1 MHz |                                                                                                                                                                                                                                                                             |
| E-UTRA Band 41                        | 2496 – 2690 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                                 |
| E-UTRA Band 42                        | 3400 – 3600 MHz | +16 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 22.                                                                                                                                                                                                |
| E-UTRA Band 43                        | 3600 – 3800 MHz | +16 dBm | 2 CW carriers | 1 MHz |                                                                                                                                                                                                                                                                             |

NOTE 1: The co-location requirements in Table 11.2.1-1 do not apply when the repeaters pass band frequency range is adjacent to the frequency range of the co-location requirement in the Table 11.2.1-1. The current state-of-the-art technology does not allow a single generic solution for co-location with other system on adjacent frequencies for 30dB Repeater-BS minimum coupling loss. However, there are certain site-engineering solutions that can be used. These techniques are addressed in TR 25.942 [5].

NOTE 2: The Table 11.2.1-1 assumes that two operating bands, where the corresponding eNode B transmit and receive frequency ranges in Table 5.5-1 would be overlapping, are not deployed in the same geographical area. For such a case of operation with overlapping frequency arrangements in the same geographical area, special co-location requirements may apply that are not covered by the 3GPP specifications.

## 11.3 Co-existence with other systems

This additional input intermodulation requirement may be applied when GSM900, DCS1800, PCS1900, GSM850, UTRA FDD, UTRA TDD and/or E-UTRA BS operating in another frequency band co-exist with an E-UTRA FDD Repeater.

Unless otherwise stated this requirement applies to the uplink and downlink of the repeater, at maximum gain.

### 11.3.1 Minimum requirement

For the parameters specified in table 11.3.1-1, the power in the pass band shall not increase with more than 10 dB at the output of the repeater as measured in the centre of the pass band, compared to the level obtained without interfering signals applied.

The frequency separation between the two interfering signals shall be adjusted so that the lowest order intermodulation product is positioned in the centre of the pass band.

NOTE 1: The lowest intermodulation products correspond to the 4<sup>th</sup> and 3<sup>rd</sup> order for the GSM 900 and DCS 1800 bands, respectively.

**Table 11.3.1-1: Input intermodulation requirements for interfering signals in co-existing other systems**

| Co-existence with other systems                    | Frequency of interfering signals | Interfering Signal Levels | Type of signals | Measurement bandwidth | Note                                                                                                                                                                                                                                                          |
|----------------------------------------------------|----------------------------------|---------------------------|-----------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GSM900                                             | 876 - 915 MHz                    | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |
| DCS1800                                            | 1710 - 1785 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 3, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |
| PCS1900                                            | 1850 - 1910 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 11.1.                                                                                                     |
| GSM850 or CDMA850                                  | 824 - 849 MHz                    | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |
| UTRA FDD Band I or E-UTRA Band 1                   | 1920 - 1980 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 1, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |
| UTRA FDD Band II or E-UTRA Band 2                  | 1850 - 1910 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25, since it is already covered by the requirement in sub-clause 11.1.                                                                                                     |
| UTRA FDD Band III or E-UTRA Band 3                 | 1710 - 1785 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 3 or band 9, since it is already covered by the requirement in sub-clause 11.1.                                                                                                      |
| UTRA FDD Band IV or E-UTRA Band 4                  | 1710 - 1755 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 4 or band 10, since it is already covered by the requirement in sub-clause 11.1.                                                                                                     |
| UTRA FDD Band V or E-UTRA Band 5                   | 824 - 849 MHz                    | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 5, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |
| UTRA FDD Band VI or XIX or E-UTRA Band 6, 18 or 19 | 815 - 830 MHz                    | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 18, since it is already covered by the requirement in sub-clause 11.1. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, 6, 19 or 20.        |
|                                                    | 830 - 845 MHz                    | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 6 or band 19, since it is already covered by the requirement in sub-clause 11.1. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 5, 18 or 20. |
| UTRA FDD Band VII or E-UTRA Band 7                 | 2500 - 2570 MHz                  | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 7, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |
| UTRA FDD Band VIII or E-UTRA Band 8                | 880 - 915 MHz                    | -15 dBm                   | 2 CW carriers   | 1 MHz                 | This requirement does not apply to E-UTRA FDD Repeater operating in band 8, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                |

|                                                 |                     |         |               |       |                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------|---------------------|---------|---------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UTRA FDD Band IX or E-UTRA Band 9               | 1749.9 - 1784.9 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 3 or band 9, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                        |
| UTRA FDD Band X or E-UTRA Band 10               | 1710 - 1770 MHz     | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 4 or band 10, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                       |
| UTRA FDD Band XI or XXI or E-UTRA Band 11 or 21 | 1427.9 - 1447.9 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 11, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
|                                                 | 1447.9 - 1462.9 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 21, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| UTRA FDD Band XII or E-UTRA Band 12             | 698 - 716 MHz       | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 12, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| UTRA FDD Band XIII or E-UTRA Band 13            | 777 - 787 MHz       | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 13, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| UTRA FDD Band XIV or E-UTRA Band 14             | 788 - 798 MHz       | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 14, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| E-UTRA Band 17                                  | 704 - 716 MHz       | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 17, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| UTRA FDD Band XX or E-UTRA Band 20              | 832 - 862 MHz       | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 20, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| UTRA FDD Band XXII or E-UTRA Band 22            | 3410 - 3490 MHz     | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 22, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| E-UTRA Band 23                                  | 2000 - 2020 MHz     | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 23, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| E-UTRA Band 24                                  | 1626.5 –1660.5 MHz  | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 24, since it is already covered by the requirement in sub-clause 11.1.                                                                                                                                 |
| UTRA FDD Band XXV or E-UTRA Band 25             | 1850 - 1915 MHz     | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 25, since it is already covered by the requirement in sub-clause 11.1. For E-UTRA FDD Repeater operating in band 2, it applies for 1910 MHz to 1915 MHz, while the rest is covered in sub-clause 11.1. |
| UTRA TDD in Band a) or E-UTRA Band 33           | 1900 - 1920 MHz     | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                    |
| UTRA TDD in Band a) or E-UTRA Band 34           | 2010 - 2025 MHz     | -15 dBm | 2 CW carriers | 1 MHz |                                                                                                                                                                                                                                                                                 |

|                                       |                 |         |               |       |                                                                                                                                                                                                                                                                       |
|---------------------------------------|-----------------|---------|---------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UTRA TDD in Band b) or E-UTRA Band 35 | 1850 – 1910 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 3 or band 9. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 2 or band 25.                                                            |
| UTRA TDD in Band b) or E-UTRA Band 36 | 1930 – 1990 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the downlink of E-UTRA FDD Repeater operating in band 2 or band 25. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1.                                                                      |
| UTRA TDD in Band c) or E-UTRA Band 37 | 1910 - 1930 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 2 or band 25. This requirement does not apply to the uplink of E-UTRA FDD Repeater operating in band 1. This unpaired band is defined in ITU-R M.1036, but is pending any future deployment. |
| UTRA TDD in Band d) or E-UTRA Band 38 | 2570 – 2620 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to the uplink E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                |
| UTRA TDD in Band f) or E-UTRA Band 39 | 1880 – 1920 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 1, band 2 or band 25.                                                                                                                                                                        |
| UTRA TDD in Band e) or E-UTRA Band 40 | 2300 – 2400 MHz | -15 dBm | 2 CW carriers | 1 MHz |                                                                                                                                                                                                                                                                       |
| E-UTRA Band 41                        | 2496 – 2690 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 7.                                                                                                                                                                                           |
| E-UTRA Band 42                        | 3400 – 3600 MHz | -15 dBm | 2 CW carriers | 1 MHz | This requirement does not apply to E-UTRA FDD Repeater operating in band 22.                                                                                                                                                                                          |
| E-UTRA Band 43                        | 3600 – 3800 MHz | -15 dBm | 2 CW carriers | 1 MHz |                                                                                                                                                                                                                                                                       |

NOTE 1: The co-existence requirements in Table 11.3.1-1 do not apply when the repeaters pass band frequency range is adjacent to the frequency range of the co-existence requirement in the Table 11.3.1-1. The current state-of-the-art technology does not allow a single generic solution for co-existence.

NOTE 2: The Table 11.3.1-1 assumes that two operating bands, where the frequency ranges in Table 5.5-1 would be overlapping, are not deployed in the same geographical area. For such a case of operation with overlapping frequency arrangements in the same geographical area, special co-existence requirements may apply that are not covered by the 3GPP specifications.

# 12 Output intermodulation

The output intermodulation requirement is a measure of the ability of the repeater to inhibit the generation of intermodulation products signals created by the presence of an interfering signal reaching the repeater via the output port.

The requirement shall apply to the downlink of the Repeater.

## 12.1 Minimum requirement

The output intermodulation level is the power of the intermodulation products when an interfering signal is injected into the output port. The wanted signal channel bandwidth  $BW_{Channel}$  shall be the maximum bandwidth supported by the repeater. The offset of the interfering signal from the wanted signal shall be as in Table 12.1-1.

**Table 12.1-1 Interfering and wanted signals for the output intermodulation requirement**

| Parameter                                                                              | Value                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wanted signal                                                                          | E-UTRA signal of maximum channel bandwidth $BW_{Channel}$                                                                                                                                         |
| Interfering signal type                                                                | E-UTRA signal of channel bandwidth 5 MHz                                                                                                                                                          |
| Interfering signal level                                                               | Mean power level 30 dB below the mean power of the wanted signal                                                                                                                                  |
| Interfering signal centre frequency offset from wanted signal carrier centre frequency | $-BW_{Channel} / 2 - 12.5$ MHz<br>$-BW_{Channel} / 2 - 7.5$ MHz<br>$-BW_{Channel} / 2 - 2.5$ MHz<br>$BW_{Channel} / 2 + 2.5$ MHz<br>$BW_{Channel} / 2 + 7.5$ MHz<br>$BW_{Channel} / 2 + 12.5$ MHz |
| NOTE:                                                                                  | Interfering signal positions that are partially or completely outside of the downlink operating band of the repeater are excluded from the requirement.                                           |

The output intermodulation level shall not exceed the unwanted emission limits in clause 9 in the presence of an interfering signal according to Table 12.1-1. The measurement may be limited to frequencies on which third and fifth order intermodulation products appear, considering the width of these products.

# 13 Adjacent Channel Rejection Ratio (ACRR)

## 13.1 Definitions and applicability

Adjacent Channel Rejection Ratio (ACRR) is the ratio of the RRC weighted gain per carrier of the repeater in the pass band to the RRC weighted gain of the repeater on an adjacent channel outside the repeater pass band. The carrier in the pass band and in the adjacent channel shall be of the same type (reference carrier).

The requirement shall apply to the uplink and downlink of the Repeater, at maximum gain, where the donor link is maintained via antennas (over the air Repeater).

### 13.1.1 Minimum Requirements

There is no minimum requirement for E-UTRA signals.

## 13.2 Co-existence with UTRA

This requirement shall be applied for the protection of UTRA signals in geographic areas in which E-UTRA-FDD Repeater and UTRA BS are deployed so that they serve adjacent channels. The reference carrier is a UTRA-FDD carrier.

### 13.2.1. Minimum Requirements

In normal conditions the ACRR shall be higher than the value specified in the Table 13.2.1-1.

**Table 13.2.1-1: Repeater ACRR**

| Co-existence with other systems | Repeater maximum output power | Channel offset from the centre frequency of the first or last 5MHz channel within the pass band. | ACRR limit |
|---------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------|------------|
| UTRA                            | $P \geq 31$ dBm               | 5 MHz                                                                                            | 33dB       |
|                                 | $P \geq 31$ dBm               | 10 MHz                                                                                           | 33dB       |
|                                 | $P < 31$ dBm                  | 5 MHz                                                                                            | 20dB       |
|                                 | $P < 31$ dBm                  | 10 MHz                                                                                           | 20dB       |

Note1: Repeater maximum output power as defined in TS25.143 clause 9.1.1.

Note2: For co-existence with TDD, a narrow band requirement is for further study.

# --- Annex A (normative): Environmental requirements for the Repeater equipment

The Repeater equipment shall fulfil all the requirements in the full range of environmental conditions for the relevant environmental class from the relevant IEC specifications listed below

- 60 721-3-3 "Stationary use at weather protected locations" [7];
- 60 721-3-4 "Stationary use at non weather protected locations" [8].

Normally it is sufficient for all tests to be conducted using normal test conditions except where otherwise stated. For guidance on the use of test conditions to be used in order to show compliance refer to TS 36.143.

# Annex B (informative): Change history

| Change history |                |           |     |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |        |        |
|----------------|----------------|-----------|-----|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|
| Date           | TSG #          | TSG Doc.  | CR  | Rev | Subject/Comment                                                                                                                                                                                                                                                                                                                                                                                                                                              | Old    | New    |
| 2008-05        | RAN4#47        | R4-080859 |     |     | TS skeleton created from 3GPP TS template.                                                                                                                                                                                                                                                                                                                                                                                                                   |        | 0.0.1  |
| 2008-06        | RAN4#47<br>bis | R4-080484 |     |     | TS skeleton with the TP agreed at RAN4#47<br>R4-080860 Text proposal 36.106: Frequency band and channel arrangement<br>R4-080861 Text proposal 36.106: Output Power<br>R4-080862 Text proposal 36.106: Out of band gain<br>R4-080863 Text proposal 36.106: Input Intermodulation                                                                                                                                                                             | 0.0.1  | 0.1.0  |
| 2008-08        | RAN4#48        | R4-081754 |     |     | TS with the TP agreed at RAN4#47bis<br>R4-081488 Text proposal 36.106: Clause3 Definition<br>R4-081490 Text proposal 36.106: Frequency stability<br>R4-081491 Text proposal 36.106: Operating band unwanted emissions<br>R4-081639 Text proposal 36.106: Spurious emissions<br>R4-081640 Text proposal 36.106:ACRR<br>R4-081641 Text proposal 36.106: Input intermodulation co-existence and co-location<br>R4-081642 Text proposal 36.106: Clause 4 General | 0.1.0  | 0.2.0  |
| 2008-08        | RAN4#48        | R4-081755 |     |     | TS with the TP agreed at RAN4#48<br>R4-081756 Text proposal 36.106: Unwanted emissions<br>R4-081856 Text proposal 36.106: Output Intermodulation<br>R4-082040 Text proposal 36.106: Annex D Environmental req.<br>Presentation to TSG                                                                                                                                                                                                                        | 0.2.0  | 1.0.0  |
| 2008-10        | RAN4#48<br>bis | R4-082274 |     |     | R4-082273 Protection of the BS receiver in the operating band:<br>Sortorder changed                                                                                                                                                                                                                                                                                                                                                                          | 1.0.0  | 1.1.0  |
| 2008-11        | RAN4#49        | R4-082900 |     |     | TS with the TP agreed at RAN4#48bis<br>R4-082397Correction to the figure with the Transmission Bandwidth Configuration                                                                                                                                                                                                                                                                                                                                       | 1.1.0  | 1.2.0  |
| 2008-11        | RAN4#49        | R4-082912 |     |     | TS with the Text proposals agreed at RAN4#49<br>R4-082902 TS36.106 Out of band gain correction<br>R4-083143 TS36.106: Operating band unwanted emission: Correction of formula<br>R4-083143 TS36.106 Clean up<br>Presentation to TSG RAN                                                                                                                                                                                                                      | 1.2.0  | 1.3.0  |
| 2008-12        | RAN #42        | RP-080864 |     |     | Approved in TSG RAN                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2.0.0  | 8.0.0  |
| 2009-03        | RAN #43        | RP-090191 | 1   |     | Alignment with 36.143 conformance testing                                                                                                                                                                                                                                                                                                                                                                                                                    | 8.0.0  | 8.1.0  |
| 2009-03        | RAN #43        | RP-090191 | 2   |     | Clarification of PHS band including the future plan                                                                                                                                                                                                                                                                                                                                                                                                          | 8.0.0  | 8.1.0  |
| 2009-03        | RAN #43        | RP-090191 | 3   | 1   | Introduction of EVM                                                                                                                                                                                                                                                                                                                                                                                                                                          | 8.0.0  | 8.1.0  |
| 2009-03        | RAN #43        | RP-090191 | 5   |     | Clarification of EARFCN for 36.106                                                                                                                                                                                                                                                                                                                                                                                                                           | 8.0.0  | 8.1.0  |
| 2009-05        | RAN #44        | RP-090552 | 6   |     | Alignment with test spec and clean-up                                                                                                                                                                                                                                                                                                                                                                                                                        | 8.1.0  | 8.2.0  |
| 2009-05        | RAN #44        | RP-090552 | 7   |     | Frequency stability                                                                                                                                                                                                                                                                                                                                                                                                                                          | 8.1.0  | 8.2.0  |
| 2009-09        | RAN #45        | RP-090819 | 9   |     | EVM for LTE Repeater                                                                                                                                                                                                                                                                                                                                                                                                                                         | 8.2.0  | 8.3.0  |
| 2009-09        | RAN #45        | RP-090819 | 8   |     | Introduction of band 17                                                                                                                                                                                                                                                                                                                                                                                                                                      | 8.2.0  | 8.3.0  |
| 2009-12        | RAN #46        | RP-091282 | 10  |     | Update of operating band unwanted emissions for LTE Repeater                                                                                                                                                                                                                                                                                                                                                                                                 | 8.3.0  | 8.4.0  |
|                |                |           |     |     | Automatic upgrade from previous Release                                                                                                                                                                                                                                                                                                                                                                                                                      | 8.4.0  | 9.0.0  |
| 2010-03        | RAN #47        | RP-100262 | 14  | 1   | Adding missing references                                                                                                                                                                                                                                                                                                                                                                                                                                    | 9.0.0  | 9.1.0  |
| 2010-09        | RAN #49        | RP-100925 | 015 |     | Introduction of operating band 18, 19, 20 and 21 and correction of band 11.                                                                                                                                                                                                                                                                                                                                                                                  | 9.1.0  | 9.2.0  |
| 2010-12        | RP #50         | RP-101333 | 021 |     | Clarification on emission requirements                                                                                                                                                                                                                                                                                                                                                                                                                       | 9.2.0  | 9.3.0  |
| 2010-12        | RP #50         | RP-101336 | 019 |     | Protection of CDMA                                                                                                                                                                                                                                                                                                                                                                                                                                           | 9.2.0  | 9.3.0  |
| 2010-12        | RP #50         | RP-101337 | 023 |     | Removal of brackets                                                                                                                                                                                                                                                                                                                                                                                                                                          | 9.2.0  | 9.3.0  |
| 2010-12        | RP #50         | RP-101347 | 016 |     | Corrections to the symbols and abbreviations clause related to DTT requirement                                                                                                                                                                                                                                                                                                                                                                               | 9.2.0  | 9.3.0  |
| 2010-12        | RP #50         | RP-101347 | 017 |     | Co-existence with services in adjacent frequency bands                                                                                                                                                                                                                                                                                                                                                                                                       | 9.2.0  | 9.3.0  |
| 2010-12        | RP #50         |           |     |     | Automatic upgrade from previous Release                                                                                                                                                                                                                                                                                                                                                                                                                      | 9.3.0  | 10.0.0 |
| 2011-04        | RP-51          | RP-110360 | 024 | 2   | Adding Band 24 specification to TS36.106                                                                                                                                                                                                                                                                                                                                                                                                                     | 10.0.0 | 10.1.0 |
| 2011-12        | RP-54          | RP-111734 | 025 | 1   | Introduction of operating frequency band 22                                                                                                                                                                                                                                                                                                                                                                                                                  | 10.1.0 | 10.2.0 |
| 2011-12        | RP-54          | RP-111734 | 027 |     | Introduction of protection limits towards frequency band 41, 42 and 43                                                                                                                                                                                                                                                                                                                                                                                       | 10.1.0 | 10.2.0 |
| 2012-03        | RP-55          | RP-120303 | 029 | 1   | Introduction of operating frequency bands 23 and 25                                                                                                                                                                                                                                                                                                                                                                                                          | 10.2.0 | 10.3.0 |
| 2012-03        | RP-55          | RP-120303 | 031 |     | Correction on the table of Regional requirements                                                                                                                                                                                                                                                                                                                                                                                                             | 10.2.0 | 10.3.0 |
| 06-2012        | RP-56          | RP-120780 | 034 |     | Definition clause updates with improved repeater pass band definition and introduction of minor editorial changes for for better alignment with BS core specification                                                                                                                                                                                                                                                                                        | 10.3.0 | 10.4.0 |

|         |       |           |     |   |                                                                                                                                               |        |        |
|---------|-------|-----------|-----|---|-----------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|
| 06-2012 | RP-56 | RP-120783 | 035 |   | Update of the upper frequency limit for Spurious Emissions                                                                                    | 10.3.0 | 10.4.0 |
| 06-2012 | RP-56 | RP-120783 | 036 | 1 | Update of the protection limits tables for spurious emission and input intermodulation                                                        | 10.3.0 | 10.4.0 |
| 06-2012 | RP-56 | RP-120762 | 040 |   | Correction of PHS protection requirements for TS 36.106                                                                                       | 10.3.0 | 10.4.0 |
| 09-2012 | RP-57 | RP-121312 | 041 |   | Update on the upper frequency limit for Spurious Emissions for Repeater                                                                       | 10.4.0 | 10.5.0 |
| 09-2012 | RP-57 | RP-121313 | 042 | 1 | Introduction of missing uplink Spurious Emission limits for E-UTRA Band 36, 41 and 42                                                         | 10.4.0 | 10.5.0 |
| 2012-09 | SP-57 | -         | -   | - | Update to Rel-11 version (MCC)                                                                                                                | 10.5.0 | 11.0.0 |
| 2012-09 | RP-57 |           |     |   | Editorial correction in Table 11.3.1-1                                                                                                        | 11.0.0 | 11.0.1 |
| 2012-12 | RP-58 | RP-121858 | 045 |   | Modifications of frequency ranges for E-UTRA Band 6, 18, 19 in the Tables for Spurious Emission limits and Input Intermodulation requirements | 11.0.1 | 11.1.0 |
| 2012-12 | RP-58 | RP-121867 | 046 |   | The special cases for protection of E-UTRA Band 3 and Band 10 in co-existence and co-location with E-UTRA Repeaters                           | 11.0.1 | 11.1.0 |
| 2012-12 | RP-58 | RP-121867 | 048 |   | The special cases for protection of E-UTRA Band 42 in co-existence and co-location with E-UTRA FDD Repeaters                                  | 11.0.1 | 11.1.0 |
| 03-2013 | RP-59 | RP-130268 | 050 |   | Co-existence between adjacent FDD and TDD bands                                                                                               | 11.1.0 | 11.2.0 |