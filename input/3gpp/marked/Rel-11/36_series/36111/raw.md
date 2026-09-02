





# Contents

|                                                                                                           |    |
|-----------------------------------------------------------------------------------------------------------|----|
| Foreword .....                                                                                            | 6  |
| 1 Scope.....                                                                                              | 7  |
| 2 References.....                                                                                         | 7  |
| 3 Definitions, symbols and abbreviations.....                                                             | 7  |
| 3.1 Definitions.....                                                                                      | 7  |
| 3.1A Symbols.....                                                                                         | 7  |
| 3.2 Abbreviations .....                                                                                   | 8  |
| 4 General.....                                                                                            | 8  |
| 5 LMU RF Requirements.....                                                                                | 8  |
| 5.1 General .....                                                                                         | 8  |
| 5.1.1 Detection probability requirement and false alarm requirement.....                                  | 10 |
| 5.1.2 Operating bands.....                                                                                | 10 |
| 5.1.3 Operating bands.....                                                                                | 11 |
| 5.2 Reference sensitivity level .....                                                                     | 13 |
| 5.2.1 Minimum requirement.....                                                                            | 13 |
| 5.3 Dynamic range .....                                                                                   | 13 |
| 5.3.1 Minimum requirement.....                                                                            | 13 |
| 5.4 In-channel selectivity .....                                                                          | 13 |
| 5.4.1 Minimum requirement.....                                                                            | 14 |
| 5.5 Adjacent Channel Selectivity (ACS) and narrow-band blocking .....                                     | 14 |
| 5.5.1 Minimum requirement.....                                                                            | 14 |
| 5.6 Blocking.....                                                                                         | 15 |
| 5.6.1 General blocking requirement .....                                                                  | 15 |
| 5.6.1.1 Minimum requirement .....                                                                         | 16 |
| 5.7 Receiver spurious emissions .....                                                                     | 17 |
| 5.7.1 Minimum requirement.....                                                                            | 17 |
| 5.8 Receiver intermodulation .....                                                                        | 17 |
| 5.8.1 Minimum requirement.....                                                                            | 17 |
| 6 UL RTOA Measurement Time Requirements .....                                                             | 18 |
| 6.1 General .....                                                                                         | 18 |
| 6.2 Requirements.....                                                                                     | 19 |
| 6.2.1 Requirements for FDD without DRX.....                                                               | 19 |
| 6.2.2 Requirements for TDD without DRX .....                                                              | 20 |
| 6.2.3 UL RTOA Measurements upon Receiving SRS Configuration Update .....                                  | 20 |
| 6.2.4 UL RTOA Measurements when Dropped SRS occurs .....                                                  | 21 |
| 6.3 Measurement Reporting Delay.....                                                                      | 21 |
| 7 UL RTOA Measurement Accuracy Requirements .....                                                         | 21 |
| 7.1 General .....                                                                                         | 21 |
| 7.2 UL RTOA measurement accuracy .....                                                                    | 21 |
| 7.2.1 UL RTOA measurement accuracy for a UE not configured with CA .....                                  | 21 |
| 7.2.2 UL RTOA measurement accuracy for a UE configured with CA.....                                       | 22 |
| 7.2.3 UL RTOA measurement accuracy when LMU is performing multiple UL RTOA measurements in parallel ..... | 23 |
| 7.2.3.1 Parallel UL RTOA measurements on the same carrier frequency.....                                  | 23 |
| 7.2.3.2 Parallel UL RTOA measurements over two carrier frequencies .....                                  | 24 |

|                               |                                                         |           |
|-------------------------------|---------------------------------------------------------|-----------|
| 8                             | UL RTOA Measurement Report Mapping .....                | 25        |
| 9                             | Search Window for UL RTOA Measurements.....             | 25        |
| <b>Annex A (informative):</b> | <b>Reference Measurement Channel.....</b>               | <b>27</b> |
| <b>Annex B (informative):</b> | <b>Propagation Conditions .....</b>                     | <b>31</b> |
| B.1                           | Static Propagation condition .....                      | 31        |
| B.2                           | Multi-path fading propagation conditions.....           | 31        |
| <b>Annex C (informative):</b> | <b>Characteristics of the interfering signals .....</b> | <b>32</b> |
| Annex D (informative):        | Change history.....                                     | 33        |

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

# 1 Scope

The present document establishes the Location Measurement Unit (LMU) minimum UTDOA positioning requirement for the FDD and TDD mode of E-UTRAN.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.
- For a specific reference, subsequent revisions do not apply.
- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document *in the same Release as the present document*.

- [1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".
- [2] 3GPP TS 36.305: "Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Stage 2 functional specification of User Equipment (UE) positioning in E-UTRAN".
- [3] 3GPP TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer; Measurements".
- [4] 3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".
- [5] 3GPP TS 36.459: "Evolved Universal Terrestrial Radio Access Network (E-UTRAN); SLm interface Application Protocol (SLmAP)".
- [6] 3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation".
- [7] 3GPP TS 36.104: "Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception".

# 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] apply.

## 3.1A Symbols

For the purposes of the present document, the following symbols apply:

|                       |                                                                                                                                                                                                           |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $BW_{\text{Channel}}$ | Channel bandwidth                                                                                                                                                                                         |
| $BW_{\text{SRS}}$     | SRS bandwidth                                                                                                                                                                                             |
| $\hat{E}_s$           | Received energy per RE (power normalized to the subcarrier spacing) during the useful part of the symbol, i.e. excluding the cyclic prefix, at the LMU antenna connector                                  |
| $I_o$                 | The total received power density, including signal and interference, as measured at the UE antenna connector                                                                                              |
| $I_{ot}$              | The received power spectral density of the total noise and interference for a certain RE (power integrated over the RE and normalized to the subcarrier spacing) as measured at the LMU antenna connector |
| $P_{\text{REFSENS}}$  | The reference sensitivity power level                                                                                                                                                                     |
| $T_{\text{SRS}}$      | The SRS periodicity in ms                                                                                                                                                                                 |

$T_s$  The basic unit of time defined in TS 36.211 clause 4

## 3.2 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

|         |                                                    |
|---------|----------------------------------------------------|
| ACS     | Adjacent Channel Selectivity                       |
| DRX     | Discontinuous Reception                            |
| E-UTRAN | Evolved Universal Terrestrial Radio Access Network |
| eNodeB  | evolved Node B                                     |
| E-SMLC  | Enhanced Serving Mobile Location Center            |
| ICS     | In-channel Selectivity                             |
| LMU     | Location Measurement Unit                          |
| SRS     | Sounding Reference Signal                          |
| UE      | User Equipment                                     |
| UL      | Uplink                                             |
| UTDOA   | Uplink Time Difference Of Arrival                  |

# --- 4 General

The UTDOA architecture is described in TS 36.305 [2].

An LMU may be deployed in three ways:

- LMU class 1: LMU integrated into base station
- LMU class 2: LMU co-sited with base station and sharing antenna with the base station
- LMU class 3: standalone LMU with own receive antenna

# --- 5 LMU RF Requirements

## 5.1 General

The requirements in clause 5 are expressed for a single receiver antenna connector. For receivers with antenna diversity, the requirements apply for each receiver antenna connector.

When the LMU is configured to receive multiple carriers for one or more UEs, all RF requirements are applicable for each received carrier. For ACS, blocking and intermodulation characteristics, the negative offsets of the interfering signal apply relative to the lower edge and positive offsets of the interfering signal apply relative to the higher edge.

Receiver test ports for LMU class 1 are illustrated in Figure 5.1-1. Receiver test ports for LMU class 2 are illustrated in Figure 5.1-2. Receiver test ports for LMU class 3 are illustrated in Figure 5.1-3. If any external apparatus, e.g., a RX amplifier, a filter or the combination of such devices is used, LMU RF requirements specified in this specification apply at the far end antenna connector (port B); otherwise, the requirements apply at port A.

Requirements applicability for different LMU classes is summarized in Table 5.1-1.

![Two block diagrams showing receiver test ports for LMU class 1. The top diagram shows a BS cabinet with an internal LMU connected to an External LNA and an External device (e.g., RX filter). Test port A is at the BS cabinet/LMU interface, and Test port B is at the External device interface. The bottom diagram shows a BS node with an RX Access Port connected to an external LNA and an External Device (if any). An LMU node is connected to the BS node. Test port A is at the LMU node interface, and Test port B is at the External Device interface.](d0abac95583b52a3b35f74a215567334_img.jpg)

The top diagram illustrates a receiver chain for LMU class 1. It consists of a **BS cabinet** containing an **LMU** (indicated by dashed lines), an **External LNA (if any)**, and an **External device e.g. RX filter (if any)**. Signal flow is from right to left, starting **From antenna connector**. **Test port A BS** and **Test port A LMU** are located at the interface between the BS cabinet and the External LNA. **Test port B BS** and **Test port B LMU** are located at the interface between the External device and the External LNA.

The bottom diagram shows another receiver chain for LMU class 1. It features a **BS node** with an **RX Access Port** connected to an **external LNA** and an **External Device (if any)**. Signal flow is from right to left, starting **From antenna connector**. An **LMU node** is connected to the **BS node**. **Test port A LMU** is at the interface between the BS node and the LMU node. **Test port B BS** and **Test port B LMU** are at the interface between the External Device and the external LNA.

Two block diagrams showing receiver test ports for LMU class 1. The top diagram shows a BS cabinet with an internal LMU connected to an External LNA and an External device (e.g., RX filter). Test port A is at the BS cabinet/LMU interface, and Test port B is at the External device interface. The bottom diagram shows a BS node with an RX Access Port connected to an external LNA and an External Device (if any). An LMU node is connected to the BS node. Test port A is at the LMU node interface, and Test port B is at the External Device interface.

Figure 5.1-1: Two examples of receiver test ports for LMU class 1.

![Block diagram showing receiver test ports for LMU class 2. A BS node is connected to a directional coupler or antenna sharing combiner, which is then connected to an external LNA and an External Device (if any). Signal flow is from right to left, starting from an antenna connector. An LMU node is connected to the directional coupler. Test port A is at the directional coupler/LMU node interface, and Test port B is at the External Device interface.](c0e88e4bd3a209b66ee7cb67e1cec2be_img.jpg)

This diagram illustrates a receiver chain for LMU class 2. It consists of a **BS node** connected to a block labeled **e.g. Directional Coupler or Antenna Sharing Combiner**. This block is connected to an **external LNA** and an **External Device (if any)**. Signal flow is from right to left, starting **From antenna connector**. An **LMU node** is connected to the **Directional Coupler or Antenna Sharing Combiner**. **test port A LMU** is at the interface between the directional coupler and the LMU node. **Test port B BS** and **Test port B LMU** are at the interface between the External Device and the external LNA.

Block diagram showing receiver test ports for LMU class 2. A BS node is connected to a directional coupler or antenna sharing combiner, which is then connected to an external LNA and an External Device (if any). Signal flow is from right to left, starting from an antenna connector. An LMU node is connected to the directional coupler. Test port A is at the directional coupler/LMU node interface, and Test port B is at the External Device interface.

Figure 5.1-2: Receiver test ports for LMU class 2.

![Figure 5.1-3: Receiver test ports for LMU class 3. The diagram shows a signal flow from left to right: LMU, External LNA (if any), and External device e.g. RX filter (if any). Test port A is indicated by an arrow pointing to the input of the LMU. Test port B is indicated by an arrow pointing to the output of the External device. A dashed line with an arrow labeled 'From antenna connector' points to the input of the External device.](b3baf3a29b67c7425d2562ddbc52f0cc_img.jpg)

Figure 5.1-3: Receiver test ports for LMU class 3. The diagram shows a signal flow from left to right: LMU, External LNA (if any), and External device e.g. RX filter (if any). Test port A is indicated by an arrow pointing to the input of the LMU. Test port B is indicated by an arrow pointing to the output of the External device. A dashed line with an arrow labeled 'From antenna connector' points to the input of the External device.

Figure 5.1-3: Receiver test ports for LMU class 3.

Table 5.1-1: Test ports and RF requirements applicability

| LMU class | Physical Node | RF Requirements                                                                                                                              | Test Port | Comments                                         |
|-----------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------|
| 1         | BS            | TS 36.104                                                                                                                                    | A or B    | Test port determined per TS 36.104               |
| 2         | BS            | Degradation of the base station DL performance and base station UL performance may occur when LMU class 2 is co-sited with the base station. | B         | Test port determined per TS 36.104               |
|           | LMU           | clauses 5.2-5.8                                                                                                                              | A or B    | Test port determined per TS 36.111, Figure 5.1-2 |
| 3         | LMU           | clauses 5.2-5.8                                                                                                                              | A or B    | Test port determined per TS 36.111, Figure 5.1-3 |

### 5.1.1 Detection probability requirement and false alarm requirement

The performance metrics used in RF requirements are detection probability and false alarm. The probability of detection is defined as the ratio of received measurement reports to the total number of measurement requests. The false alarm rate is the probability of detection of a signal that is not present, and is defined as the percentage of the received measurement reports to the total number of measurement requests with the measurement configuration of a signal that is not present. The detection probability requirement is 99% and the false alarm requirement is 0.1%. The detection probability requirement and the false alarm requirement apply for any number of receive ports, any channel bandwidth, and all frame structures.

### 5.1.2 Operating bands

E-UTRA LMUs may operate in one or more of the operating bands defined in Table 5.1.2-1.

**Table 5.1.2-1: E-UTRA frequency bands**

| E-UTRA Operating Band | Uplink (UL) operating band                 | Downlink (DL) operating band               | Duplex Mode      |
|-----------------------|--------------------------------------------|--------------------------------------------|------------------|
|                       | BS receive<br>UE transmit                  | BS transmit<br>UE receive                  |                  |
|                       | F <sub>UL_low</sub> – F <sub>UL_high</sub> | F <sub>DL_low</sub> – F <sub>DL_high</sub> |                  |
| 1                     | 1920 MHz – 1980 MHz                        | 2110 MHz – 2170 MHz                        | FDD              |
| 2                     | 1850 MHz – 1910 MHz                        | 1930 MHz – 1990 MHz                        | FDD              |
| 3                     | 1710 MHz – 1785 MHz                        | 1805 MHz – 1880 MHz                        | FDD              |
| 4                     | 1710 MHz – 1755 MHz                        | 2110 MHz – 2155 MHz                        | FDD              |
| 5                     | 824 MHz – 849 MHz                          | 869 MHz – 894 MHz                          | FDD              |
| 6 <sup>1</sup>        | 830 MHz – 840 MHz                          | 875 MHz – 885 MHz                          | FDD              |
| 7                     | 2500 MHz – 2570 MHz                        | 2620 MHz – 2690 MHz                        | FDD              |
| 8                     | 880 MHz – 915 MHz                          | 925 MHz – 960 MHz                          | FDD              |
| 9                     | 1749.9 MHz – 1784.9 MHz                    | 1844.9 MHz – 1879.9 MHz                    | FDD              |
| 10                    | 1710 MHz – 1770 MHz                        | 2110 MHz – 2170 MHz                        | FDD              |
| 11                    | 1427.9 MHz – 1447.9 MHz                    | 1475.9 MHz – 1495.9 MHz                    | FDD              |
| 12                    | 699 MHz – 716 MHz                          | 729 MHz – 746 MHz                          | FDD              |
| 13                    | 777 MHz – 787 MHz                          | 746 MHz – 756 MHz                          | FDD              |
| 14                    | 788 MHz – 798 MHz                          | 758 MHz – 768 MHz                          | FDD              |
| 15                    | Reserved                                   | Reserved                                   | FDD              |
| 16                    | Reserved                                   | Reserved                                   | FDD              |
| 17                    | 704 MHz – 716 MHz                          | 734 MHz – 746 MHz                          | FDD              |
| 18                    | 815 MHz – 830 MHz                          | 860 MHz – 875 MHz                          | FDD              |
| 19                    | 830 MHz – 845 MHz                          | 875 MHz – 890 MHz                          | FDD              |
| 20                    | 832 MHz – 862 MHz                          | 791 MHz – 821 MHz                          |                  |
| 21                    | 1447.9 MHz – 1462.9 MHz                    | 1495.9 MHz – 1510.9 MHz                    | FDD              |
| 22                    | 3410 MHz – 3490 MHz                        | 3510 MHz – 3590 MHz                        | FDD              |
| 23                    | 2000 MHz – 2020 MHz                        | 2180 MHz – 2200 MHz                        | FDD              |
| 24                    | 1626.5 MHz – 1660.5 MHz                    | 1525 MHz – 1559 MHz                        | FDD              |
| 25                    | 1850 MHz – 1915 MHz                        | 1930 MHz – 1995 MHz                        | FDD              |
| 26                    | 814 MHz – 849 MHz                          | 859 MHz – 894 MHz                          | FDD              |
| 27                    | 807 MHz – 824 MHz                          | 852 MHz – 869 MHz                          | FDD              |
| 28                    | 703 MHz – 748 MHz                          | 758 MHz – 803 MHz                          | FDD              |
| 29                    | N/A                                        | 717 MHz – 728 MHz                          | FDD <sup>2</sup> |
| ...                   |                                            |                                            |                  |
| 33                    | 1900 MHz – 1920 MHz                        | 1900 MHz – 1920 MHz                        | TDD              |
| 34                    | 2010 MHz – 2025 MHz                        | 2010 MHz – 2025 MHz                        | TDD              |
| 35                    | 1850 MHz – 1910 MHz                        | 1850 MHz – 1910 MHz                        | TDD              |
| 36                    | 1930 MHz – 1990 MHz                        | 1930 MHz – 1990 MHz                        | TDD              |
| 37                    | 1910 MHz – 1930 MHz                        | 1910 MHz – 1930 MHz                        | TDD              |
| 38                    | 2570 MHz – 2620 MHz                        | 2570 MHz – 2620 MHz                        | TDD              |
| 39                    | 1880 MHz – 1920 MHz                        | 1880 MHz – 1920 MHz                        | TDD              |
| 40                    | 2300 MHz – 2400 MHz                        | 2300 MHz – 2400 MHz                        | TDD              |
| 41                    | 2496 MHz – 2690 MHz                        | 2496 MHz – 2690 MHz                        | TDD              |
| 42                    | 3400 MHz – 3600 MHz                        | 3400 MHz – 3600 MHz                        | TDD              |
| 43                    | 3600 MHz – 3800 MHz                        | 3600 MHz – 3800 MHz                        | TDD              |
| 44                    | 703 MHz – 803 MHz                          | 703 MHz – 803 MHz                          | TDD              |

NOTE 1: Band 6 is not applicable.

NOTE 2: Restricted to E-UTRA operation when carrier aggregation is configured. The downlink operating band is paired with the uplink operating band (external) of the carrier aggregation configuration that is supporting the configured PCell.

### 5.1.3 Operating bands

LMU requirements are for the channel bandwidths listed in Table 5.1.3-1.

**Table 5.1.3-1: Transmission bandwidth configuration  $N_{RB}$  in E-UTRA channel bandwidths**

|                                                                     |     |    |    |    |    |     |
|---------------------------------------------------------------------|-----|----|----|----|----|-----|
| <b>Channel bandwidth<br/><math>BW_{Channel}</math> [MHz]</b>        | 1.4 | 3  | 5  | 10 | 15 | 20  |
| <b>Transmission bandwidth<br/>configuration <math>N_{RB}</math></b> | 6   | 15 | 25 | 50 | 75 | 100 |

Figure 5.1.3-1 shows the relation between the Channel bandwidth ( $BW_{Channel}$ ) and the Transmission bandwidth configuration ( $N_{RB}$ ). The channel edges are defined as the lowest and highest frequencies of the carrier separated by the channel bandwidth, i.e. at  $F_C \pm BW_{Channel} / 2$ .

![Figure 5.1.3-1: Definition of Channel Bandwidth and Transmission Bandwidth Configuration for one E-UTRA carrier. The diagram shows a horizontal axis representing frequency. A central group of blue vertical bars represents 'Active Resource Blocks'. Above this group, a double-headed arrow labeled 'Transmission Bandwidth Configuration [RB]' spans the width of the active blocks. Above that, a wider double-headed arrow labeled 'Transmission Bandwidth [RB]' also spans the active blocks. The entire group of blocks is flanked by dashed vertical lines labeled 'Channel edge'. A horizontal double-headed arrow at the top, spanning from the left channel edge to the right channel edge, is labeled 'Channel Bandwidth [MHz]'. Below the active blocks, a bracket labeled 'Active Resource Blocks' is shown. A dashed vertical line in the center of the active blocks is labeled 'Center subcarrier (corresponds to DC in baseband) is not transmitted in downlink'.](5e92d9e8e9ce204e405bff2367f88176_img.jpg)

Figure 5.1.3-1: Definition of Channel Bandwidth and Transmission Bandwidth Configuration for one E-UTRA carrier. The diagram shows a horizontal axis representing frequency. A central group of blue vertical bars represents 'Active Resource Blocks'. Above this group, a double-headed arrow labeled 'Transmission Bandwidth Configuration [RB]' spans the width of the active blocks. Above that, a wider double-headed arrow labeled 'Transmission Bandwidth [RB]' also spans the active blocks. The entire group of blocks is flanked by dashed vertical lines labeled 'Channel edge'. A horizontal double-headed arrow at the top, spanning from the left channel edge to the right channel edge, is labeled 'Channel Bandwidth [MHz]'. Below the active blocks, a bracket labeled 'Active Resource Blocks' is shown. A dashed vertical line in the center of the active blocks is labeled 'Center subcarrier (corresponds to DC in baseband) is not transmitted in downlink'.

**Figure 5.1.3-1: Definition of Channel Bandwidth and Transmission Bandwidth Configuration for one E-UTRA carrier.**

Figure 5.1.3-2 illustrates the aggregated channel bandwidth for intra-band carrier aggregation.

![Figure 5.1.3-2: Definition of Aggregated Channel Bandwidth for intra-band carrier aggregation. The diagram shows three separate carrier blocks on a frequency axis. The leftmost block has a central subcarrier labeled F_C_low and a transmission bandwidth configuration spanning several resource blocks. The rightmost block has a central subcarrier labeled F_C_high and a similar transmission bandwidth configuration. The middle block is highlighted in green. The overall width from the leftmost channel edge to the rightmost channel edge is labeled 'Aggregated Channel Bandwidth, BW_Channel_CA [MHz]'. The leftmost edge is labeled 'Lower Edge' and 'F_edge_low'. The rightmost edge is labeled 'Higher Edge' and 'F_edge_high'. The distance from F_C_low to F_edge_low is labeled F_offset. Similarly, the distance from F_C_high to F_edge_high is labeled F_offset. A note at the bottom states: 'For each carrier, the center sub carrier (corresponds to DC in baseband) is not transmitted in downlink'.](7c6d9bfe9c31ce872722d60b73d20df1_img.jpg)

Figure 5.1.3-2: Definition of Aggregated Channel Bandwidth for intra-band carrier aggregation. The diagram shows three separate carrier blocks on a frequency axis. The leftmost block has a central subcarrier labeled F\_C\_low and a transmission bandwidth configuration spanning several resource blocks. The rightmost block has a central subcarrier labeled F\_C\_high and a similar transmission bandwidth configuration. The middle block is highlighted in green. The overall width from the leftmost channel edge to the rightmost channel edge is labeled 'Aggregated Channel Bandwidth, BW\_Channel\_CA [MHz]'. The leftmost edge is labeled 'Lower Edge' and 'F\_edge\_low'. The rightmost edge is labeled 'Higher Edge' and 'F\_edge\_high'. The distance from F\_C\_low to F\_edge\_low is labeled F\_offset. Similarly, the distance from F\_C\_high to F\_edge\_high is labeled F\_offset. A note at the bottom states: 'For each carrier, the center sub carrier (corresponds to DC in baseband) is not transmitted in downlink'.

**Figure 5.1.3-2: Definition of Aggregated Channel Bandwidth for intra-band carrier aggregation**

The lower edge of the Aggregated Channel Bandwidth ( $BW_{Channel\_CA}$ ) is defined as  $F_{edge\_low} = F_{C\_low} - F_{offset}$ . The upper edge of the aggregated channel bandwidth is defined as  $F_{edge\_high} = F_{C\_high} + F_{offset}$ . The Aggregated Channel Bandwidth,  $BW_{Channel\_CA}$ , is defined as follows:

$$BW_{Channel\_CA} = F_{edge\_high} - F_{edge\_low} \text{ [MHz]}$$

## 5.2 Reference sensitivity level

The reference sensitivity power level  $P_{\text{REFSENS}}$  is the minimum mean power received at the antenna connector at which a detection probability requirement and a false alarm requirement shall be met for a specified reference measurement channel.

### 5.2.1 Minimum requirement

The LMU shall receive the reference measurement channel while meeting the detection probability and false alarm requirement in clause 5.1.1. The reference measurement channel is described in Table 5.2.1-1 with parameters specified in Annex A.

**Table 5.2.1-1: LMU reference sensitivity levels**

| E-UTRA channel bandwidth [MHz] | Reference measurement channel | Reference sensitivity power level, $P_{\text{REFSENS}}$ [dBm] |
|--------------------------------|-------------------------------|---------------------------------------------------------------|
| 1.4                            | Annex A                       | -130.8                                                        |
| 3                              | Annex A                       | -130.8                                                        |
| 5                              | Annex A                       | -130.8                                                        |
| 10                             | Annex A                       | -130.8                                                        |
| 15                             | Annex A                       | -130.8                                                        |
| 20                             | Annex A                       | -130.8                                                        |

## 5.3 Dynamic range

The dynamic range is specified as a measure of the capability of the receiver to receive a wanted signal in the presence of an interfering signal inside the received channel bandwidth. In this condition, a detection probability requirement and a false alarm requirement shall be met for a specified reference measurement channel. The interfering signal for the dynamic range requirement is an AWGN signal.

### 5.3.1 Minimum requirement

The LMU shall receive the reference measurement channel while meeting the detection probability and false alarm requirement in clause 5.1.1. The reference measurement channel is described in Table 5.2.1-1 with parameters specified in Annex A.

**Table 5.3.1-1: LMU dynamic range**

| E-UTRA channel bandwidth [MHz] | Reference measurement channel | Wanted signal mean power [dBm] | Interfering signal mean power [dBm] / $BW_{\text{Config}}$ | Type of interfering signal |
|--------------------------------|-------------------------------|--------------------------------|------------------------------------------------------------|----------------------------|
| 1.4                            | Annex A                       | -108.5                         | -88.7                                                      | AWGN                       |
| 3                              | Annex A                       | -104.6                         | -84.7                                                      | AWGN                       |
| 5                              | Annex A                       | -102.4                         | -82.5                                                      | AWGN                       |
| 10                             | Annex A                       | -99.4                          | -79.5                                                      | AWGN                       |
| 15                             | Annex A                       | -97.6                          | -77.7                                                      | AWGN                       |
| 20                             | Annex A                       | -96.3                          | -76.4                                                      | AWGN                       |

## 5.4 In-channel selectivity

In-channel selectivity (ICS) is a measure of the receiver ability to receive a wanted signal at its assigned resource block locations in the presence of an interfering signal received at a larger power spectral density. In this condition, a detection probability requirement and a false alarm requirement shall be met for a specified reference measurement channel. The interfering signal shall be an E-UTRA signal as specified in Annex C and shall be time aligned with the wanted signal.

### 5.4.1 Minimum requirement

The LMU shall receive the reference measurement channel while meeting the detection probability and false alarm requirement in clause 5.1.1. The reference measurement channel is specified in Annex A with parameters specified in Table 5.2.1-1.

**Table 5.4.1-1 E-UTRA LMU in-channel selectivity**

| E-UTRA channel bandwidth (MHz) | Reference measurement channel | Wanted signal mean power [dBm] | Interfering signal mean power [dBm] | Type of interfering signal                    |
|--------------------------------|-------------------------------|--------------------------------|-------------------------------------|-----------------------------------------------|
| 1.4                            | Annex A                       | -127.8                         | -91                                 | 1.4 MHz E-UTRA PUCCH signal, 2 RBs (see note) |
| 3                              | Annex A                       | -127.8                         | -85                                 | 3 MHz E-UTRA PUSCH signal, 4 RBs (see note)   |
| 5                              | Annex A                       | -127.8                         | -85                                 | 5 MHz E-UTRA PUSCH signal, 4 RBs (see note)   |
| 10                             | Annex A                       | -127.8                         | -85                                 | 10 MHz E-UTRA PUSCH signal, 4 RBs (see note)  |
| 15                             | Annex A                       | -127.8                         | -85                                 | 15 MHz E-UTRA PUSCH signal, 4 RBs (see note)  |
| 20                             | Annex A                       | -127.8                         | -85                                 | 20 MHz E-UTRA PUSCH signal, 4 RBs (see note)  |

NOTE: Except for the 1.4 MHz channel the wanted and interfering signal are placed adjacently around  $F_c$ . For the 1.4 MHz channel the PUCCH interferer is placed at the two edge resource blocks in the channel each having the specified signal power.

## 5.5 Adjacent Channel Selectivity (ACS) and narrow-band blocking

Adjacent channel selectivity (ACS) is a measure of the receiver ability to receive a wanted signal at its assigned channel frequency in the presence of an adjacent channel signal with a specified centre frequency offset of the interfering signal to the band edge of a victim system. In this condition a detection probability requirement and a false alarm requirement shall be met for a specified reference measurement channel. The interfering signal shall be an E-UTRA signal as specified in Annex C.

### 5.5.1 Minimum requirement

The LMU shall receive the reference measurement channel while meeting the detection probability and false alarm requirement in clause 5.1.1. The reference measurement channel is specified in Annex A with parameters specified in Table 5.2.1-1.

The wanted and the interfering signal coupled to the BS antenna input are specified in Tables 5.5.1-1 and 5.5.1-2 for narrowband blocking and in Table 5.5.1-3 for ACS. The reference measurement channel for the wanted signal is identified in Table 5.2.1-1 for each channel bandwidth and further specified in Annex A.

**Table 5.5.1-1: Narrowband blocking requirement**

| Wanted signal mean power [dBm] | Interfering signal mean power [dBm] | Type of interfering signal |
|--------------------------------|-------------------------------------|----------------------------|
| PREFSENS + 13 dB               | -49                                 | See Table 5.5.1-2          |

**Table 5.5.1-2: Interfering signal for Narrowband blocking requirement**

| E-UTRA channel BW of the lowest (highest) carrier received [MHz] | Interfering RB centre frequency offset to the lower (higher) edge [kHz] | Type of interfering signal                |
|------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------|
| 1.4                                                              | $\pm(252.5+m*180)$ ,<br>m=0, 1, 2, 3, 4, 5                              | 1.4 MHz E-UTRA signal, 1 RB<br>(see note) |
| 3                                                                | $\pm(247.5+m*180)$ ,<br>m=0, 1, 2, 3, 4, 7, 10, 13                      | 3 MHz E-UTRA signal, 1 RB<br>(see note)   |
| 5                                                                | $\pm(342.5+m*180)$ ,<br>m=0, 1, 2, 3, 4, 9, 14, 19, 24                  | 5 MHz E-UTRA signal, 1 RB<br>(see note)   |
| 10                                                               | $\pm(347.5+m*180)$ ,<br>m=0, 1, 2, 3, 4, 9, 14, 19, 24                  | 5 MHz E-UTRA signal, 1 RB<br>(see note)   |
| 15                                                               | $\pm(352.5+m*180)$ ,<br>m=0, 1, 2, 3, 4, 9, 14, 19, 24                  | 5 MHz E-UTRA signal, 1 RB<br>(see note)   |
| 20                                                               | $\pm(342.5+m*180)$ ,<br>m=0, 1, 2, 3, 4, 9, 14, 19, 24                  | 5 MHz E-UTRA signal, 1 RB<br>(see note)   |

NOTE: Interfering signal consisting of one resource block is positioned at the stated offset; the channel bandwidth of the interfering signal is located adjacently to the lower (upper) edge.

**Table 5.5.1-3: LMU Adjacent channel selectivity**

| E-UTRA channel bandwidth of the lowest (highest) carrier received [MHz] | Wanted signal mean power [dBm] | Interfering signal mean power [dBm] | Interfering signal centre frequency offset from the lower (higher) edge [MHz] | Type of interfering signal  |
|-------------------------------------------------------------------------|--------------------------------|-------------------------------------|-------------------------------------------------------------------------------|-----------------------------|
| 1.4                                                                     | P <sub>REFSENS</sub> + 13 dB   | -52                                 | $\pm 0.7025$                                                                  | 1.4 MHz E-UTRA signal 4 RBs |
| 3                                                                       | P <sub>REFSENS</sub> + 13 dB   | -52                                 | $\pm 1.5075$                                                                  | 3 MHz E-UTRA signal 4 RBs   |
| 5                                                                       | P <sub>REFSENS</sub> + 13 dB   | -52                                 | $\pm 2.5025$                                                                  | 5 MHz E-UTRA signal 4 RBs   |
| 10                                                                      | P <sub>REFSENS</sub> + 13 dB   | -52                                 | $\pm 2.5075$                                                                  | 5 MHz E-UTRA signal 4 RBs   |
| 15                                                                      | P <sub>REFSENS</sub> + 13 dB   | -52                                 | $\pm 2.5125$                                                                  | 5 MHz E-UTRA signal 4 RBs   |
| 20                                                                      | P <sub>REFSENS</sub> + 13 dB   | -52                                 | $\pm 2.5025$                                                                  | 5 MHz E-UTRA signal 4 RBs   |

## 5.6 Blocking

### 5.6.1 General blocking requirement

The blocking characteristics is a measure of the receiver ability to receive a wanted signal at its assigned channel in the presence of an unwanted interferer, which are either a 1.4 MHz, 3 MHz or 5 MHz E-UTRA signal for in-band blocking or a CW signal for out-of-band blocking. In this condition, a detection probability requirement and a false alarm requirement shall be met for a specified reference measurement channel. The interfering signal shall be an E-UTRA signal as specified in Annex C.

#### 5.6.1.1 Minimum requirement

The LMU shall receive the reference measurement channel while meeting the detection probability and false alarm requirement in clause 5.1.1, with a wanted and an interfering signal coupled to the LMU antenna input using the parameters in Tables 5.6.1.1-1, 5.6.1.1-1a, 5.6.1.1-1b and 5.6.1.1-2. The reference measurement channel for the wanted signal is identified in Table 5.2.1-1 for each channel bandwidth and further specified in Annex A.

**Table 5.6.1.1-1: LMU Blocking performance requirement**

| Operating Band                                    | Centre Frequency of Interfering Signal [MHz]                          | Interfering Signal mean power [dBm] | Wanted Signal mean power [dBm] | Interfering signal centre frequency minimum frequency offset from the lower (higher) edge [MHz] | Type of Interfering Signal |
|---------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------|----------------------------|
| 1-7, 9-11, 13, 14, 18, 19, 21-23, 24, 27, 33-4344 | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +20)               | -43                                 | P <sub>REFSENS</sub> +13 dB    | See table 5.6.1.1-2                                                                             | See table 5.6.1.1-2        |
|                                                   | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +20) to 12750 | -15                                 | P <sub>REFSENS</sub> +13 dB    | —                                                                                               | CW carrier                 |
| 8, 26, 28                                         | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +10)               | -43                                 | P <sub>REFSENS</sub> +13 dB    | See table 5.6.1.1-2                                                                             | See table 5.6.1.1-2        |
|                                                   | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +10) to 12750 | -15                                 | P <sub>REFSENS</sub> +13 dB    | —                                                                                               | CW carrier                 |
| 12                                                | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +13)               | -43                                 | P <sub>REFSENS</sub> +13 dB    | See table 5.6.1.1-2                                                                             | See table 5.6.1.1-2        |
|                                                   | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +13) to 12750 | -15                                 | P <sub>REFSENS</sub> +13 dB    | —                                                                                               | CW carrier                 |
| 17                                                | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +18)               | -43                                 | P <sub>REFSENS</sub> +13 dB    | See table 5.6.1.1-2                                                                             | See table 5.6.1.1-2        |
|                                                   | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +18) to 12750 | -15                                 | P <sub>REFSENS</sub> +13 dB    | —                                                                                               | CW carrier                 |
| 20                                                | (F <sub>UL_low</sub> -11) to (F <sub>UL_high</sub> +20)               | -43                                 | P <sub>REFSENS</sub> +13 dB    | See table 5.6.1.1-2                                                                             | See table 5.6.1.1-2        |
|                                                   | 1 to (F <sub>UL_low</sub> -11)<br>(F <sub>UL_high</sub> +20) to 12750 | -15                                 | P <sub>REFSENS</sub> +13 dB    | —                                                                                               | CW carrier                 |
| 25                                                | (F <sub>UL_low</sub> -20) to (F <sub>UL_high</sub> +15)               | -43                                 | P <sub>REFSENS</sub> +13 dB    | See table 5.6.1.1-2                                                                             | See table 5.6.1.1-2        |
|                                                   | 1 to (F <sub>UL_low</sub> -20)<br>(F <sub>UL_high</sub> +15) to 12750 | -15                                 | P <sub>REFSENS</sub> +13 dB    | —                                                                                               | CW carrier                 |

NOTE: Table 5.6.1.1-1 assumes that two operating bands, where the downlink operating band (see Table 5.5-1 of TS 36.104) of one band would be within the in-band blocking region of the other band, are not deployed in the same geographical area.

**Table 5.6.1.1-2: Interfering signals for blocking performance requirement**

| E-UTRA channel BW of the lowest (highest) carrier received [MHz] | Interfering signal centre frequency minimum offset to the lower (higher) edge [MHz] | Type of interfering signal  |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------|
| 1.4                                                              | ±2.1                                                                                | 1.4 MHz E-UTRA signal 4 RBs |
| 3                                                                | ±4.5                                                                                | 3 MHz E-UTRA signal 4 RBs   |
| 5                                                                | ±7.5                                                                                | 5 MHz E-UTRA signal 4 RBs   |
| 10                                                               | ±7.5                                                                                | 5 MHz E-UTRA signal 4 RBs   |
| 15                                                               | ±7.5                                                                                | 5 MHz E-UTRA signal 4 RBs   |
| 20                                                               | ±7.5                                                                                | 5 MHz E-UTRA signal 4 RBs   |

## 5.7 Receiver spurious emissions

The spurious emissions power is the power of emissions generated or amplified in a receiver that appear at the LMU receiver antenna connector. The requirement specified in this clause, is to reduce the impact on a co-sited BS, a different BS, or a different LMU.

### 5.7.1 Minimum requirement

The power of any spurious emission shall not exceed the levels in Table 5.7.1-1.

**Table 5.7.1-1: General spurious emission minimum requirement**

| Frequency range                                                                                  | Maximum level | Measurement Bandwidth | Note                                  |
|--------------------------------------------------------------------------------------------------|---------------|-----------------------|---------------------------------------|
| 30MHz - 1 GHz                                                                                    | -57 dBm       | 100 kHz               |                                       |
| 1 GHz – 12.75 GHz                                                                                | -47 dBm       | 1 MHz                 |                                       |
| 12.75 GHz - 5 <sup>th</sup> harmonic of the upper frequency edge of the UL operating band in GHz | -47 dBm       | 1 MHz                 | Applies only for Bands 22, 42 and 43. |

NOTE 1: The frequency range between  $2.5 \cdot BW_{\text{Channel}}$  below the first carrier frequency and  $2.5 \cdot BW_{\text{Channel}}$  above the last carrier frequency, where  $BW_{\text{Channel}}$  is the channel bandwidth, may be excluded from the requirement. However, frequencies that are more than 10 MHz below the lowest frequency of the downlink operating band or more than 10 MHz above the highest frequency of the downlink operating band shall not be excluded from the requirement.

NOTE 2: The requirements apply only if the isolation between LMU receiver and BS is 30 dB or more. If the isolation is less, the emissions may be higher which may impact performance.

In addition to the requirements in Table 5.7.1-1, the power of any spurious emission shall not exceed the levels specified for Protection of the E-UTRA FDD BS receiver of own or different BS in TS 36.104, clause 6.6.4.2 and for Co-existence with other systems in the same geographical area in TS 36.104, clause 6.6.4.3. In addition, the co-existence requirements for co-located base stations specified in TS 36.104, clause 6.6.4.4 may also be applied for LMUs co-sited with a BS, co-located with a different BS, or with another LMU.

## 5.8 Receiver intermodulation

Third and higher order mixing of the two interfering RF signals can produce an interfering signal in the band of the desired channel. Intermodulation response rejection is a measure of the capability of the receiver to receive a wanted signal on its assigned channel frequency in the presence of two interfering signals which have a specific frequency relationship to the wanted signal. In this condition, a detection probability requirement and a false alarm requirement shall be met for a specified reference measurement channel. Interfering signals shall be a CW signal and an E-UTRA signal as specified in Annex C.

### 5.8.1 Minimum requirement

The LMU shall receive the reference measurement channel while meeting the detection probability and false alarm requirement in clause 5.1.1, with a wanted signal at the assigned channel frequency and two interfering signals coupled to the LMU antenna input, with the conditions specified in Tables 5.8.1-1 and 5.8.1-2 for intermodulation performance and in Tables 5.8.1-3, 5.8.1-4 and Table 5.8.1-5 for narrowband intermodulation performance. The reference measurement channel for the wanted signal is identified in Table 5.2.1-1 for each channel bandwidth and further specified in Annex A.

**Table 5.8.1-1: Intermodulation performance requirement**

| Wanted signal mean power [dBm] | Interfering signal mean power [dBm] | Type of interfering signal |
|--------------------------------|-------------------------------------|----------------------------|
| PREFSENS + 13dB                | -52                                 | See Table 5.8.1-2          |

**Table 5.8.1-2: Interfering signal for Intermodulation performance requirement**

| E-UTRA channel bandwidth of the lowest (highest) carrier received [MHz] | Interfering signal centre frequency offset from the lower (higher) edge [MHz] | Type of interfering signal   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------|
| 1.4                                                                     | ±2.1                                                                          | CW                           |
|                                                                         | ±4.9                                                                          | 1.4 MHz E-UTRA signal, 4 RBs |
| 3                                                                       | ±4.5                                                                          | CW                           |
|                                                                         | ±10.5                                                                         | 3 MHz E-UTRA signal, 12 RBs  |
| 5                                                                       | ±7.5                                                                          | CW                           |
|                                                                         | ±17.5                                                                         | 5 MHz E-UTRA signal, 20 RBs  |
| 10                                                                      | ±7.375                                                                        | CW                           |
|                                                                         | ±17.5                                                                         | 5 MHz E-UTRA signal, 20 RBs  |
| 15                                                                      | ±7.25                                                                         | CW                           |
|                                                                         | ±17.5                                                                         | 5 MHz E-UTRA signal, 20 RBs  |
| 20                                                                      | ±7.125                                                                        | CW                           |
|                                                                         | ±17.5                                                                         | 5 MHz E-UTRA signal, 20 RBs  |

**Table 5.8.1-3: Narrowband intermodulation performance requirement for LMU**

| E-UTRA channel bandwidth of the lowest (highest) carrier received [MHz] | Wanted signal mean power [dBm] | Interfering signal mean power [dBm] | Interfering RB centre frequency offset from the lower (higher) edge [kHz] | Type of interfering signal             |
|-------------------------------------------------------------------------|--------------------------------|-------------------------------------|---------------------------------------------------------------------------|----------------------------------------|
| 1.4                                                                     | P <sub>REFSENS</sub> + 7dB     | -52                                 | ±270                                                                      | CW                                     |
|                                                                         |                                | -52                                 | ±790                                                                      | 1.4 MHz E-UTRA signal, 1 RB (see note) |
| 3                                                                       | P <sub>REFSENS</sub> + 11dB    | -52                                 | ±270                                                                      | CW                                     |
|                                                                         |                                | -52                                 | ±780                                                                      | 3.0 MHz E-UTRA signal, 1 RB (see note) |
| 5                                                                       | P <sub>REFSENS</sub> + 13dB    | -52                                 | 360                                                                       | CW                                     |
|                                                                         |                                | -52                                 | ±1060                                                                     | 5 MHz E-UTRA signal, 1 RB (see note)   |
| 10                                                                      | P <sub>REFSENS</sub> + 13dB    | -52                                 | ±325                                                                      | CW                                     |
|                                                                         |                                | -52                                 | ±1240                                                                     | 5 MHz E-UTRA signal, 1 RB (see note)   |
| 15                                                                      | P <sub>REFSENS</sub> + 13dB    | -52                                 | ±380                                                                      | CW                                     |
|                                                                         |                                | -52                                 | ±1600                                                                     | 5MHz E-UTRA signal, 1 RB (see note)    |
| 20                                                                      | P <sub>REFSENS</sub> + 13dB    | -52                                 | ±345                                                                      | CW                                     |
|                                                                         |                                | -52                                 | ±1780                                                                     | 5MHz E-UTRA signal, 1 RB (see note)    |

NOTE: Interfering signal consisting of one resource block positioned at the stated offset, the channel bandwidth of the interfering signal is located adjacently to the lower (upper) edge.

# 6 UL RTOA Measurement Time Requirements

## 6.1 General

The requirements described in clause 6 apply to UL RTOA timing measurements performed by LMU for UL positioning based on SRS signals transmitted by the UE, TS 36.214 [3]. The SRS signal transmissions used for UL RTOA measurements may be configured for other purpose than UL positioning, before or after the UL positioning session starts.

The LMU shall be able to perform UL RTOA measurements in all supported bands and meet the corresponding requirements in clause 6.2.

An LMU shall be capable to perform parallel UL RTOA measurements:

- An LMU shall be capable to perform in parallel UL RTOA measurements for at least 32 UEs, and
- An LMU shall be capable to perform in parallel at least 16 UL RTOA measurements per uplink carrier frequency for different UEs, and
- A multi-carrier capable LMU shall be able to perform in parallel UL RTOA measurements, on multiple carriers, where the carriers may belong to the same E-UTRA frequency band or to different E-UTRA frequency bands.

A CA-capable LMU shall be able to perform measurements for UEs configured with UL CA.

## 6.2 Requirements

For all measurements performed in parallel according to the LMU measurement capability requirements, the UL RTOA measurement accuracy shall be fulfilled according to the accuracy requirements as specified in clause 7.

The requirements for UL RTOA measurements for UE not configured with DRX are specified in clauses 6.2.1 and 6.2.2 for FDD and TDD, respectively.

A UE configured with DRX does not transmit instances of periodic SRS while not in Active Time state, TS 36.321 [4].

In this LTE release:

- UL RTOA measurements may fail when the UE is configured with DRX while the UL RTOA measurements are performed by LMUs.
- UL RTOA measurement requirements for UE configured with DRX are not specified.

### 6.2.1 Requirements for FDD without DRX

The LMU shall be able to perform UL RTOA measurements in all supported FDD bands and meet the requirements in this clause.

The LMU shall be able to perform and report a UE's UL RTOA measurements, based in its SRS transmissions, within  $T_{\text{RTOA,E-UTRAN FDD, nonDRX}}$  ms as given below:

$$T_{\text{RTOA,E-UTRAN FDD, nonDRX}} = T_{\text{SRS}} \cdot (M - 1) \cdot \left\lceil \frac{n}{N} \right\rceil + \Delta \text{ ms},$$

- where  $T_{\text{SRS}}$  is the SRS periodicity in ms, according to the *srsConfiguration* IE received by the LMU from the E-SMLC via SLmAP [5];
- $M$  is the number of SRS measurement occasions (depends on the applicable bandwidth);
- $n$  is the number of requested UL RTOA measurements per carrier;
- $N$  is the minimum number of UL RTOA measurements per uplink carrier frequency for different UEs that can be measured in parallel, and
- $\Delta=50$  ms is a margin to account e.g. for the time necessary for sampling and processing.

An SRS measurement occasion is a subframe that may contain SRS, according to the *srsConfiguration* IE received by LMU from E-SMLC via SLmAP [5]. The UE may drop some SRSs transmissions (see clause 6.2.4).

The same required measurement time  $T_{\text{RTOA,E-UTRAN FDD, nonDRX}}$  applies irrespective of whether parallel UL RTOA measurements are requested for a single frequency carrier, multiple frequency carriers, or multiple frequency bands.

For all measurements performed in parallel according to the LMU measurement capability requirements specified in clause 6.1 and the measurement requirements specified in clause 6.2, the UL RTOA measurement accuracy shall be fulfilled according to the accuracy requirements as specified in clause 7.

Note: Parameters  $T_{\text{SRS}}$ ,  $M$  and the applicable bandwidth are as specified in clause 7.

### 6.2.2 Requirements for TDD without DRX

The LMU shall be able to perform UL RTOA measurements in all supported TDD bands and meet the requirements in this clause.

The LMU shall be able to perform and report a UE's UL RTOA measurements, based on its SRS transmissions, within  $T_{\text{RTOA,E-UTRAN TDD, nonDRX}}$  ms. When the SRS periodicity  $T_{\text{SRS}}$  is greater than 2 ms, the UL RTOA measurement requirements specified in clause 6.2.1 apply. For SRS periodicity  $T_{\text{SRS}}=2$  ms,  $T_{\text{RTOA,E-UTRAN TDD, nonDRX}}$  is as defined below:

$$T_{\text{RTOA,E-UTRAN TDD, nonDRX}} = \frac{10}{N_{\text{SP}}} \cdot \left( \frac{M}{2} + 1 \right) \cdot \left\lceil \frac{n}{N} \right\rceil + \Delta \text{ ms},$$

Where:

- $M$  is the number of SRS measurement occasions (depends on the applicable bandwidth),
- $N_{\text{SP}}$  is the number of downlink to uplink switch points in a radio frame,
- $n$  is the number of requested UL RTOA measurements per carrier,
- $N$  is the minimum number of UL RTOA measurements per uplink carrier frequency for different UEs that can be measured in parallel, and
- $\Delta= 50$  ms is a margin to account e.g. for the time necessary for sampling and processing.

An SRS measurement occasion is a subframe that may contain SRS, according to the *srsConfiguration* IE received by LMU from E-SMLC via SLmAP [5]. The UE may drop some SRSs transmissions (see clause 6.2.4).

The same required measurement time  $T_{\text{RTOA,E-UTRAN TDD, nonDRX}}$  applies irrespective of whether parallel UL RTOA measurements are requested for a single frequency carrier, multiple frequency carriers, or multiple frequency bands.

For all measurements performed in parallel according to the LMU measurement capability requirements specified in , 6.1 and the measurement requirements specified in clause 6.2, the UL RTOA measurement accuracy shall be fulfilled according to the accuracy requirements as specified in clause 7.

Note: Parameters  $T_{\text{SRS}}$ ,  $M$  and the applicable bandwidth are as specified in clause 7.

### 6.2.3 UL RTOA Measurements upon Receiving SRS Configuration Update

UE SRS configuration may change for one or more cells, or the set of cells with SRS configured for the UE may change during UL positioning.

Upon receiving an updated SRS configuration, the LMU shall continue the UL RTOA measurement for a cell and report the measurement, while meeting the requirements in Section 6, in the following two cases:

1. The new SRS configuration for the cell is the same as the SRS configuration for this cell before receiving the SRS configuration update.
2. The new SRS configuration for the cell is a superset of the SRS configuration for this cell received before the update, i.e. the updated SRS configuration comprises the SRS configuration before the update but may also have other SRS configured.

NOTE: Requirements specified in , 6 corresponding to the SRS periodicity  $T_{\text{SRS}}$  before the update apply in both cases above.

### 6.2.4 UL RTOA Measurements when Dropped SRS occurs

With or without DRX, dropped SRS may occur, e.g., due to measurement gaps, autonomous gaps, interruptions due to CA, and other channel transmissions. UL RTOA measurement performance may degrade when dropped SRS occur.

## 6.3 Measurement Reporting Delay

The requirements in clause 6 assume that the UL RTOA measurement report is not delayed by other SLmAP signalling.

# 7 UL RTOA Measurement Accuracy Requirements

## 7.1 General

All accuracy requirements in Section 7.2 shall apply under the following additional conditions:

- All configured SRS have been transmitted by the UE,
- DRX is not configured in the UE,
- The maximum transmit power adjustment in the UE during the UL RTOA measurement time is within the range of  $\pm 3.5$  dB,
- The maximum transmit timing adjustment in the UE during the UL RTOA measurement time is within the range of  $\pm 4.5$  Ts.

## 7.2 UL RTOA measurement accuracy

### 7.2.1 UL RTOA measurement accuracy for a UE not configured with CA

The UL RTOA accuracy requirements for a UE not configured with CA are defined in Table 7.2.1-1, assuming one receive antenna at LMU. The reference measurement channel is as specified in Annex A and the propagation conditions are specified in Annex B.

The requirements apply under the following conditions:

- SRS  $\hat{E}_s/I_{ot} \geq -16.9$  dB,
- Measured SRS  $\hat{E}_s/N_{oc} = -8$  dB;
- All interference and noise: AWGN,
- Minimum  $I_o -125.1$  dBm/15kHz,
- Maximum  $I_o -50.0$  dBm/BWchannel,

**Table 7.2.1-1: LMU UL RTOA measurement accuracy requirements**

| SRS bandwidth (RBs) | AWGN                                |               | EPA5                                |               | ETU30                               |               |
|---------------------|-------------------------------------|---------------|-------------------------------------|---------------|-------------------------------------|---------------|
|                     | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) |
| 4                   | 233                                 | 10            | 250                                 | 10            | 421                                 | 16            |
| 8                   | 71                                  | 8             | 77                                  | 10            | 127                                 | 14            |
| 12                  | 37                                  | 8             | 42                                  | 8             | 90                                  | 14            |
| 16                  | 24                                  | 8             | 29                                  | 10            | 63                                  | 12            |
| 20                  | 17                                  | 8             | 22                                  | 8             | 52                                  | 12            |
| 24                  | 14                                  | 8             | 18                                  | 8             | 44                                  | 12            |
| 32                  | 9                                   | 8             | 13                                  | 8             | 35                                  | 12            |
| 36                  | 8                                   | 6             | 12                                  | 8             | 32                                  | 12            |
| 40                  | 7                                   | 6             | 10                                  | 8             | 29                                  | 12            |
| 48                  | 5                                   | 6             | 9                                   | 8             | 25                                  | 12            |
| 60                  | 5                                   | 6             | 7                                   | 8             | 20                                  | 14            |
| 64                  | 4                                   | 6             | 7                                   | 8             | 18                                  | 14            |
| 72                  | 4                                   | 6             | 6                                   | 8             | 17                                  | 14            |
| 80                  | 3                                   | 6             | 6                                   | 8             | 15                                  | 14            |
| 96                  | 3                                   | 6             | 5                                   | 8             | 13                                  | 14            |

### 7.2.2 UL RTOA measurement accuracy for a UE configured with CA

The UL RTOA accuracy requirements for a UE configured with CA are defined in Table 7.2.2-1, assuming one receive antenna at LMU. The reference measurement channel is as specified in Annex A and the propagation conditions are specified in Annex B.

The requirements apply under the following conditions:

- SRS  $\hat{E}_s/I_{ot} \geq -16.9$  dB,
- Measured SRS  $\hat{E}_s/N_{oc} = -8$  dB;
- All interference and noise: AWGN,
- Minimum  $I_{ot}$  -125.1 dBm/15kHz,
- Maximum  $I_{ot}$  -50.0 dBm/BWchannel,

When the LMU is configured to measure on multiple RF carriers for a UE configured with CA, the requirements shall apply for each carrier frequency.

**Table 7.2.2-1: LMU UL RTOA measurement accuracy requirements**

| SRS bandwidth (RBs) | AWGN                                |               | EPA5                                |               | ETU30                               |               |
|---------------------|-------------------------------------|---------------|-------------------------------------|---------------|-------------------------------------|---------------|
|                     | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) |
| 4                   | 233                                 | 10            | 250                                 | 10            | 421                                 | 16            |
| 8                   | 71                                  | 8             | 77                                  | 10            | 127                                 | 14            |
| 12                  | 37                                  | 8             | 42                                  | 8             | 90                                  | 14            |
| 16                  | 24                                  | 8             | 29                                  | 10            | 63                                  | 12            |
| 20                  | 17                                  | 8             | 22                                  | 8             | 52                                  | 12            |
| 24                  | 14                                  | 8             | 18                                  | 8             | 44                                  | 12            |
| 32                  | 9                                   | 8             | 13                                  | 8             | 35                                  | 12            |
| 36                  | 8                                   | 6             | 12                                  | 8             | 32                                  | 12            |
| 40                  | 7                                   | 6             | 10                                  | 8             | 29                                  | 12            |
| 48                  | 5                                   | 6             | 9                                   | 8             | 25                                  | 12            |
| 60                  | 5                                   | 6             | 7                                   | 8             | 20                                  | 14            |
| 64                  | 4                                   | 6             | 7                                   | 8             | 18                                  | 14            |
| 72                  | 4                                   | 6             | 6                                   | 8             | 17                                  | 14            |
| 80                  | 3                                   | 6             | 6                                   | 8             | 15                                  | 14            |
| 96                  | 3                                   | 6             | 5                                   | 8             | 13                                  | 14            |

### 7.2.3 UL RTOA measurement accuracy when LMU is performing multiple UL RTOA measurements in parallel

The UL RTOA accuracy requirements for an LMU performing multiple measurements in parallel are defined in Tables 7.2.3-1 and 7.2.3-2, assuming one receive antenna at the LMU. The reference measurement channel is specified in Annex A and the propagation conditions are specified in Annex B.

#### 7.2.3.1 Parallel UL RTOA measurements on the same carrier frequency

An LMU shall be capable of performing in parallel at least 16 UL RTOA measurements per uplink carrier frequency for different UEs [see clause 6.1].

The requirements apply under the following conditions:

- SRS  $\hat{E}_s/I_{ot} \geq -16.9$  dB,
- Measured SRS  $\hat{E}_s/N_{oc} = -8$  dB;

- All interference and noise: AWGN,
- Minimum  $I_o$  -125.1 dBm/15kHz,
- Maximum  $I_o$  -50.0 dBm/BWchannel,

The requirements are specified in Table 7.2.3-1.

**Table 7.2.3-1: LMU UL RTOA measurement accuracy requirements**

| SRS bandwidth (RBs) | AWGN                                |               | EPA5                                |               | ETU30                               |               |
|---------------------|-------------------------------------|---------------|-------------------------------------|---------------|-------------------------------------|---------------|
|                     | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) |
| 4                   | 233                                 | 10            | 250                                 | 10            | 421                                 | 16            |
| 8                   | 71                                  | 8             | 77                                  | 10            | 127                                 | 14            |
| 12                  | 37                                  | 8             | 42                                  | 8             | 90                                  | 14            |
| 16                  | 24                                  | 8             | 29                                  | 10            | 63                                  | 12            |
| 20                  | 17                                  | 8             | 22                                  | 8             | 52                                  | 12            |
| 24                  | 14                                  | 8             | 18                                  | 8             | 44                                  | 12            |
| 32                  | 9                                   | 8             | 13                                  | 8             | 35                                  | 12            |
| 36                  | 8                                   | 6             | 12                                  | 8             | 32                                  | 12            |
| 40                  | 7                                   | 6             | 10                                  | 8             | 29                                  | 12            |
| 48                  | 5                                   | 6             | 9                                   | 8             | 25                                  | 12            |
| 60                  | 5                                   | 6             | 7                                   | 8             | 20                                  | 14            |
| 64                  | 4                                   | 6             | 7                                   | 8             | 18                                  | 14            |
| 72                  | 4                                   | 6             | 6                                   | 8             | 17                                  | 14            |
| 80                  | 3                                   | 6             | 6                                   | 8             | 15                                  | 14            |
| 96                  | 3                                   | 6             | 5                                   | 8             | 13                                  | 14            |

#### 7.2.3.2 Parallel UL RTOA measurements over two carrier frequencies

An LMU shall be capable of performing parallel UL RTOA measurements [see clause 6.1] for at least 32 UEs in total over all carrier frequencies and at least 16 UL RTOA measurements per uplink carrier frequency for different UEs [see clause 6.1].

The requirements apply under the following conditions:

- SRS  $\hat{E}_s/I_{ot}$  (dB)  $\geq -16.9$  dB,
- Measured SRS  $\hat{E}_s/N_{oc} = -8$  dB;
- All interference and noise: AWGN,
- Minimum  $I_o$  -125.1 dBm/15kHz,
- Maximum  $I_o$  -50.0 dBm/BWchannel,

The requirements are specified in Table 7.2.3-2.

**Table 7.2.3-2: LMU UL RTOA measurement accuracy requirements**

| SRS bandwidth (RBs) | AWGN                                |               | EPA5                                |               | ETU30                               |               |
|---------------------|-------------------------------------|---------------|-------------------------------------|---------------|-------------------------------------|---------------|
|                     | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) | Minimum number of SRS transmissions | 90% RTOA (Ts) |
| 4                   | 233                                 | 10            | 250                                 | 10            | 421                                 | 16            |
| 8                   | 71                                  | 8             | 77                                  | 10            | 127                                 | 14            |
| 12                  | 37                                  | 8             | 42                                  | 8             | 90                                  | 14            |
| 16                  | 24                                  | 8             | 29                                  | 10            | 63                                  | 12            |
| 20                  | 17                                  | 8             | 22                                  | 8             | 52                                  | 12            |
| 24                  | 14                                  | 8             | 18                                  | 8             | 44                                  | 12            |
| 32                  | 9                                   | 8             | 13                                  | 8             | 35                                  | 12            |
| 36                  | 8                                   | 6             | 12                                  | 8             | 32                                  | 12            |
| 40                  | 7                                   | 6             | 10                                  | 8             | 29                                  | 12            |
| 48                  | 5                                   | 6             | 9                                   | 8             | 25                                  | 12            |
| 60                  | 5                                   | 6             | 7                                   | 8             | 20                                  | 14            |
| 64                  | 4                                   | 6             | 7                                   | 8             | 18                                  | 14            |
| 72                  | 4                                   | 6             | 6                                   | 8             | 17                                  | 14            |
| 80                  | 3                                   | 6             | 6                                   | 8             | 15                                  | 14            |
| 96                  | 3                                   | 6             | 5                                   | 8             | 13                                  | 14            |

# 8 UL RTOA Measurement Report Mapping

The reporting range of the UL RTOA measurement is defined from  $0 \times T_s$  to  $9598 \times T_s$  with  $2 \times T_s$  resolution. The mapping of the measured quantity is defined in Table 8-1. The UL RTOA measurement is reported by the LMU to the E-SMLC via SLmAP in ULRTOAMeasurements IE.

**Table 8-1: UL RTOA measurement report mapping**

| Reported Value                                                | Measured UL RTOA, in $T_s$        |
|---------------------------------------------------------------|-----------------------------------|
| ULRTOA_0001                                                   | $0 < \text{UL RTOA} \leq 2$       |
| ULRTOA_0002                                                   | $2 < \text{UL RTOA} \leq 4$       |
| ...                                                           | ...                               |
| ULRTOA_4799                                                   | $9596 < \text{UL RTOA} \leq 9598$ |
| ULRTOA_4800                                                   | $9598 < \text{UL RTOA}$           |
| NOTE: $T_s$ is the basic timing unit as defined in TS 36.211. |                                   |

# 9 Search Window for UL RTOA Measurements

The E-SMLC may provide search window information to the LMU via the SLmAP [5], which may be used by the LMU for configuring its receiver for performing UL RTOA measurements. The search window parameters include:

- expected propagation delay  $T$  (center of the search window), and
- delay uncertainty  $\Delta$  (half width of the search window);

which together define the search window  $[T-\Delta; T+\Delta]$  centered at time  $T$ , and where  $\Delta$  may be a timing advance measurement for serving cell.

The mapping for the two search window parameters is defined in Table 9-1 and Table 9-2. The expected propagation delay is defined from  $0 \times T_s$  to  $9592 \times T_s$  with  $8 \times T_s$  resolution. The delay uncertainty is defined from  $0 \times T_s$  to  $792 \times T_s$  with  $8 \times T_s$  resolution.

**Table 9-1: Expected propagation delay mapping**

| <b>Value</b>                                                               | <b>Expected Propagation Delay T, in T<sub>s</sub></b> |
|----------------------------------------------------------------------------|-------------------------------------------------------|
| ULRTOA_exp_delay_0001                                                      | $0 < T \leq 8$                                        |
| ULRTOA_exp_delay_0002                                                      | $8 < T \leq 16$                                       |
| ...                                                                        | ...                                                   |
| ULRTOA_exp_delay_1199                                                      | $9584 < T \leq 9592$                                  |
| ULRTOA_exp_delay_1200                                                      | $9592 < T$                                            |
| NOTE: T <sub>s</sub> is the basic timing unit as defined in TS 36.211 [6]. |                                                       |

**Table 9-2: Delay uncertainty mapping**

| <b>Value</b>                                                               | <b>Delay Uncertainty Δ, in T<sub>s</sub></b> |
|----------------------------------------------------------------------------|----------------------------------------------|
| ULRTOA_uncertainty_001                                                     | $0 < \Delta \leq 8$                          |
| ULRTOA_uncertainty_002                                                     | $8 < \Delta \leq 16$                         |
| ...                                                                        | ...                                          |
| ULRTOA_uncertainty_099                                                     | $784 < \Delta \leq 792$                      |
| ULRTOA_uncertainty_100                                                     | $792 < \Delta$                               |
| NOTE: T <sub>s</sub> is the basic timing unit as defined in TS 36.211 [6]. |                                              |

# Annex A (informative): Reference Measurement Channel

Editor's note: SRS configuration, including SRS bandwidth, for UL RTOA measurement accuracy requirements is to be discussed separately and is not related to the SRS configuration in this.

**Table A-1: SRS Configuration for receiver requirements except in-channel selectivity**

| Channel bandwidth                                              | 1.4 MHz              | 3 MHz                | 5 MHz                | 10 MHz               | 15 MHz               | 20 MHz               |
|----------------------------------------------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| UL bandwidth                                                   | n6                   | n15                  | n25                  | n50                  | n75                  | n100                 |
| srsBandwidthConfiguration                                      | bw7                  | bw5                  | bw3                  | bw5                  | bw6                  | bw5                  |
| srsBandwidth                                                   | bw0                  | bw0                  | bw0                  | bw1                  | bw2                  | bw2                  |
| srsHoppingBandwidth                                            | hbw0                 | hbw0                 | hbw0                 | hbw1                 | hbw2                 | hbw2                 |
| frequencyDomainPosition                                        | 0                    | 0                    | 0                    | 2                    | 8                    | 13                   |
| srs-ConfigIndex                                                | 5                    | 5                    | 5                    | 5                    | 5                    | 5                    |
| transmissionComb                                               | 0                    | 0                    | 0                    | 0                    | 0                    | 0                    |
| cyclicShift                                                    | cs0                  | cs0                  | cs0                  | cs0                  | cs0                  | cs0                  |
| srsAntennaPort                                                 | an1                  | an1                  | an1                  | an1                  | an1                  | an1                  |
| Number of SRS resource blocks                                  | 4                    | 4                    | 4                    | 4                    | 4                    | 4                    |
| Number of configured SRS transmissions, as indicated by E-SMLC | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) |

NOTE 1: The number of SRS transmissions may also be configured as Inf.  
NOTE 2: No SRS sequence hopping, no SRS group hopping

**Table A-2: SRS Configuration for in-channel selectivity**

| Channel bandwidth                                              | 1.4 MHz              | 3 MHz                | 5 MHz                | 10 MHz               | 15 MHz               | 20 MHz               |
|----------------------------------------------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| UL bandwidth                                                   | n6                   | n15                  | n25                  | n50                  | n75                  | n100                 |
| srsBandwidthConfiguration                                      | bw7                  | bw5                  | bw5                  | bw5                  | bw6                  | bw5                  |
| srsBandwidth                                                   | bw0                  | bw1                  | bw1                  | bw1                  | bw2                  | bw2                  |
| srsHoppingBandwidth                                            | hbw0                 | hbw1                 | hbw1                 | hbw1                 | hbw2                 | hbw2                 |
| frequencyDomainPosition                                        | 0                    | 0                    | 0                    | 2                    | 5                    | 13                   |
| srs-ConfigIndex                                                | 5                    | 5                    | 5                    | 5                    | 5                    | 5                    |
| transmissionComb                                               | 0                    | 0                    | 0                    | 0                    | 0                    | 0                    |
| cyclicShift                                                    | cs0                  | cs0                  | cs0                  | cs0                  | cs0                  | cs0                  |
| srsAntennaPort                                                 | an1                  | an1                  | an1                  | an1                  | an1                  | an1                  |
| Number of SRS resource blocks                                  | 4                    | 4                    | 4                    | 4                    | 4                    | 4                    |
| Number of configured SRS transmissions, as indicated by E-SMLC | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) | ≥500<br>(see note 1) |

NOTE 1: The number of SRS transmissions may also be configured as Inf.  
NOTE 2: No SRS sequence hopping, no SRS group hopping

**Table A-3: SRS Configuration for accuracy and measurement time requirements, 4 ≤ SRS RBs ≤ 36, single UE**

|                               |         |       |       |       |       |        |        |        |
|-------------------------------|---------|-------|-------|-------|-------|--------|--------|--------|
| Number of SRS resource blocks | 4       | 8     | 12    | 16    | 20    | 24     | 32     | 36     |
| Channel bandwidth             | 1.4 MHz | 3 MHz | 3 MHz | 5 MHz | 5 MHz | 10 MHz | 10 MHz | 10 MHz |
| UL bandwidth                  | n6      | n15   | n15   | n25   | n25   | n50    | n50    | n50    |
| Physical cell ID              | 1       | 1     | 1     | 1     | 1     | 1      | 1      | 1      |
| srsBandwidthConfiguration     | bw7     | bw6   | bw5   | bw4   | bw3   | bw5    | bw4    | bw3    |
| srsBandwidth                  | bw0     | bw0   | bw0   | bw0   | bw0   | bw0    | bw0    | bw0    |
| srsHoppingBandwidth           | hbw0    | hbw0  | hbw0  | hbw0  | hbw0  | hbw0   | hbw0   | hbw0   |
| frequencyDomainPosition       | 0       | 0     | 0     | 0     | 0     | 0      | 0      | 0      |
| srs-ConfigIndex               | 325     | 325   | 325   | 325   | 325   | 325    | 325    | 325    |
| transmissionComb              | 0       | 0     | 0     | 0     | 0     | 0      | 0      | 0      |
| cyclicShift                   | cs0     | cs0   | cs0   | cs0   | cs0   | cs0    | cs0    | cs0    |
| srsAntennaPort                | an1     | an1   | an1   | an1   | an1   | an1    | an1    | an1    |

Note 1: No SRS sequence hopping, no SRS group hopping

**Table A-4: SRS Configuration for accuracy and measurement time requirements,  $40 \leq \text{SRS RBs} \leq 96$ , single UE**

|                                                       |        |        |        |        |        |        |        |
|-------------------------------------------------------|--------|--------|--------|--------|--------|--------|--------|
| Number of SRS resource blocks                         | 40     | 48     | 60     | 64     | 72     | 80     | 96     |
| Channel bandwidth                                     | 10 MHz | 10 MHz | 15 MHz | 15 MHz | 15 MHz | 20 MHz | 20 MHz |
| UL bandwidth                                          | n50    | n50    | n75    | n75    | n75    | n100   | n100   |
| Physical cell ID                                      | 1      | 1      | 1      | 1      | 1      | 1      | 1      |
| srsBandwidthConfiguration                             | bw2    | bw1    | bw2    | bw1    | bw0    | bw2    | bw1    |
| srsBandwidth                                          | bw0    | bw0    | bw0    | bw0    | bw0    | bw0    | bw0    |
| srsHoppingBandwidth                                   | hbw0   | hbw0   | hbw0   | hbw0   | hbw0   | hbw0   | hbw0   |
| frequencyDomainPosition                               | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| srs-ConfigIndex                                       | 325    | 325    | 325    | 325    | 325    | 325    | 325    |
| transmissionComb                                      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| cyclicShift                                           | cs0    | cs0    | cs0    | cs0    | cs0    | cs0    | cs0    |
| srsAntennaPort                                        | an1    | an1    | an1    | an1    | an1    | an1    | an1    |
| Note 1: No SRS sequence hopping, no SRS group hopping |        |        |        |        |        |        |        |

**Table A-5: SRS Configuration for accuracy and measurement time requirements,  $4 \leq \text{SRS RBs} \leq 36$ , parallel UL RTOA measurements**

|                                                       |         |       |       |       |       |        |        |        |
|-------------------------------------------------------|---------|-------|-------|-------|-------|--------|--------|--------|
| Number of SRS resource blocks                         | 4       | 8     | 12    | 16    | 20    | 24     | 32     | 36     |
| Channel bandwidth                                     | 1.4 MHz | 3 MHz | 3 MHz | 5 MHz | 5 MHz | 10 MHz | 10 MHz | 10 MHz |
| UL bandwidth                                          | n6      | n15   | n15   | n25   | n25   | n50    | n50    | n50    |
| srsBandwidthConfiguration                             | bw7     | bw6   | bw5   | bw4   | bw3   | bw5    | bw4    | bw3    |
| srsBandwidth                                          | bw0     | bw0   | bw0   | bw0   | bw0   | bw0    | bw0    | bw0    |
| srsHoppingBandwidth                                   | hbw0    | hbw0  | hbw0  | hbw0  | hbw0  | hbw0   | hbw0   | hbw0   |
| frequencyDomainPosition                               | 0       | 0     | 0     | 0     | 0     | 0      | 0      | 0      |
| srs-ConfigIndex                                       | 325     | 325   | 325   | 325   | 325   | 325    | 325    | 325    |
| srsAntennaPort                                        | an1     | an1   | an1   | an1   | an1   | an1    | an1    | an1    |
| Note 1: No SRS sequence hopping, no SRS group hopping |         |       |       |       |       |        |        |        |

**Table A-6: SRS Configuration for accuracy and measurement time requirements,  $40 \leq \text{SRS RBs} \leq 96$ , parallel UL RTOA measurements**

|                                                       |        |        |        |        |        |        |        |
|-------------------------------------------------------|--------|--------|--------|--------|--------|--------|--------|
| Number of SRS resource blocks                         | 40     | 48     | 60     | 64     | 72     | 80     | 96     |
| Channel bandwidth                                     | 10 MHz | 10 MHz | 15 MHz | 15 MHz | 15 MHz | 20 MHz | 20 MHz |
| UL bandwidth                                          | n50    | n50    | n75    | n75    | n75    | n100   | n100   |
| srsBandwidthConfiguration                             | bw2    | bw1    | bw2    | bw1    | bw0    | bw2    | bw1    |
| srsBandwidth                                          | bw0    | bw0    | bw0    | bw0    | bw0    | bw0    | bw0    |
| srsHoppingBandwidth                                   | hbw0   | hbw0   | hbw0   | hbw0   | hbw0   | hbw0   | hbw0   |
| frequencyDomainPosition                               | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| srs-ConfigIndex                                       | 325    | 325    | 325    | 325    | 325    | 325    | 325    |
| srsAntennaPort                                        | an1    | an1    | an1    | an1    | an1    | an1    | an1    |
| Note 1: No SRS sequence hopping, no SRS group hopping |        |        |        |        |        |        |        |

**Table A-7: SRS Physical cell ID for parallel UL RTOA measurements**

| Channel bandwidth | 1.4 MHz | 3 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz |
|-------------------|---------|-------|-------|--------|--------|--------|
| <b>UE number</b>  |         |       |       |        |        |        |
| 1                 | 1       | 1     | 1     | 1      | 1      | 1      |
| 2                 | 1       | 1     | 1     | 1      | 1      | 1      |
| 3                 | 1       | 1     | 1     | 1      | 1      | 1      |
| 4                 | 1       | 1     | 1     | 1      | 1      | 1      |
| 5                 | 2       | 1     | 1     | 1      | 1      | 1      |
| 6                 | 2       | 1     | 1     | 1      | 1      | 1      |
| 7                 | 2       | 1     | 1     | 1      | 1      | 1      |
| 8                 | 2       | 1     | 1     | 1      | 1      | 1      |
| 9                 | 3       | 2     | 1     | 1      | 1      | 1      |
| 10                | 3       | 2     | 1     | 1      | 1      | 1      |
| 11                | 3       | 2     | 1     | 1      | 1      | 1      |
| 12                | 3       | 2     | 1     | 1      | 1      | 1      |
| 13                | 4       | 2     | 1     | 1      | 1      | 1      |
| 14                | 4       | 2     | 1     | 1      | 1      | 1      |
| 15                | 4       | 2     | 1     | 1      | 1      | 1      |
| 16                | 4       | 2     | 1     | 1      | 1      | 1      |

**Table A-8: SRS cyclic shift for parallel UL RTOA measurements**

| Channel bandwidth | 1.4 MHz | 3 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz |
|-------------------|---------|-------|-------|--------|--------|--------|
| <b>UE number</b>  |         |       |       |        |        |        |
| 1                 | cs0     | cs0   | cs0   | cs0    | cs0    | cs0    |
| 2                 | cs4     | cs2   | cs1   | cs1    | cs1    | cs1    |
| 3                 | cs0     | cs4   | cs2   | cs2    | cs2    | cs2    |
| 4                 | cs4     | cs6   | cs3   | cs3    | cs3    | cs3    |
| 5                 | cs0     | cs0   | cs4   | cs4    | cs4    | cs4    |
| 6                 | cs4     | cs2   | cs5   | cs5    | cs5    | cs5    |
| 7                 | cs0     | cs4   | cs6   | cs6    | cs6    | cs6    |
| 8                 | cs4     | cs6   | cs7   | cs7    | cs7    | cs7    |
| 9                 | cs0     | cs0   | cs0   | cs0    | cs0    | cs0    |
| 10                | cs4     | cs2   | cs1   | cs1    | cs1    | cs1    |
| 11                | cs0     | cs4   | cs2   | cs2    | cs2    | cs2    |
| 12                | cs4     | cs6   | cs3   | cs3    | cs3    | cs3    |
| 13                | cs0     | cs0   | cs4   | cs4    | cs4    | cs4    |
| 14                | cs4     | cs2   | cs5   | cs5    | cs5    | cs5    |
| 15                | cs0     | cs4   | cs6   | cs6    | cs6    | cs6    |
| 16                | cs4     | cs6   | cs7   | cs7    | cs7    | cs7    |

**Table A-9: SRS transmission comb for parallel UL RTOA measurements**

| Channel bandwidth | 1.4 MHz | 3 MHz | 5 MHz | 10 MHz | 15 MHz | 20 MHz |
|-------------------|---------|-------|-------|--------|--------|--------|
| UE number         |         |       |       |        |        |        |
| 1                 | 0       | 0     | 0     | 0      | 0      | 0      |
| 2                 | 0       | 0     | 0     | 0      | 0      | 0      |
| 3                 | 1       | 0     | 0     | 0      | 0      | 0      |
| 4                 | 1       | 0     | 0     | 0      | 0      | 0      |
| 5                 | 0       | 1     | 0     | 0      | 0      | 0      |
| 6                 | 0       | 1     | 0     | 0      | 0      | 0      |
| 7                 | 1       | 1     | 0     | 0      | 0      | 0      |
| 8                 | 1       | 1     | 0     | 0      | 0      | 0      |
| 9                 | 0       | 0     | 1     | 1      | 1      | 1      |
| 10                | 0       | 0     | 1     | 1      | 1      | 1      |
| 11                | 1       | 0     | 1     | 1      | 1      | 1      |
| 12                | 1       | 0     | 1     | 1      | 1      | 1      |
| 13                | 0       | 1     | 1     | 1      | 1      | 1      |
| 14                | 0       | 1     | 1     | 1      | 1      | 1      |
| 15                | 1       | 1     | 1     | 1      | 1      | 1      |
| 16                | 1       | 1     | 1     | 1      | 1      | 1      |

# Annex B (informative): Propagation Conditions

## B.1 Static Propagation condition

The propagation for the static performance measurement is an Additive White Gaussian Noise (AWGN) environment. No fading or multi-paths exist for this propagation model.

## B.2 Multi-path fading propagation conditions

Tables B.2-1 – B.2.3 show multi-path delay profiles that are used for the performance measurements in multi-path fading environment. All taps have classical Doppler spectrum, defined as:

$$(CLASS) \quad S(f) \propto 1/(1 - (f/f_D)^2)^{0.5} \quad \text{for } f \in -f_D, f_D.$$

**Table B.2-1 Extended Pedestrian A model (EPA)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | 0.0                 |
| 30                    | -1.0                |
| 70                    | -2.0                |
| 90                    | -3.0                |
| 110                   | -8.0                |
| 190                   | -17.2               |
| 410                   | -20.8               |

**Table B.2-2 Extended Typical Urban model (ETU)**

| Excess tap delay [ns] | Relative power [dB] |
|-----------------------|---------------------|
| 0                     | -1.0                |
| 50                    | -1.0                |
| 120                   | -1.0                |
| 200                   | 0.0                 |
| 230                   | 0.0                 |
| 500                   | 0.2                 |
| 1600                  | -3.0                |
| 2300                  | -5.0                |
| 5000                  | -7.0                |

# Annex C (informative): Characteristics of the interfering signals

The interfering signal for the 1.4 MHz in-channel requirement shall be a PUCCH. For the other requirements the interferer shall be a PUSCH containing data and reference symbols. Normal cyclic prefix is used. The data content shall be uncorrelated to the wanted signal and modulated according to clause 5 of TS 36.211. Mapping of the PUCCH and PUSCH modulation to receiver requirement are specified in table C-1.1.

**Table C-1.1: Modulation of the interfering signal**

| <b>Receiver requirement</b>                              | <b>Signal/Modulation</b> |
|----------------------------------------------------------|--------------------------|
| In-channel selectivity (1.4 MHz channel)                 | PUCCH/QPSK               |
| In-channel selectivity (3, 5, 10, 15 and 20 MHz channel) | PUSCH/16QAM              |
| Adjacent channel selectivity and narrow-band blocking    | PUSCH/QPSK               |
| Blocking                                                 | PUSCH/QPSK               |
| Receiver intermodulation                                 | PUSCH/QPSK               |

# Annex D (informative): Change history

| Change history |       |           |      |     |                                                                        |        |        |
|----------------|-------|-----------|------|-----|------------------------------------------------------------------------|--------|--------|
| Date           | TSG   | Doc.      | CR   | Rev | Subject/Comment                                                        | Old    | New    |
| 03-2013        | RP-59 | RP-130317 |      |     | Presented for information at RAN#59.                                   |        | 1.0.0  |
| 06-2013        | RP-60 | RP-130839 |      |     | Presented to RAN#60 for Approval                                       |        | 1.1.1  |
| 06-2013        | RP-60 | RP-130839 |      |     | TR Approved by RAN                                                     | 1.1.1  | 11.0.0 |
| 12-2013        | RP-62 | RP-131935 | 002  | 1   | Addition of UL RTOA Measurement Accuracy Requirements to TS 36.111     | 11.0.0 | 11.1.0 |
| 03-2014        | RP-63 | RP-140373 | 003  | 2   | Modification of UL RTOA Measurement Accuracy Requirements in TS 36.111 | 11.1.0 | 11.2.0 |
| 06-2014        | RP-64 | RP-140915 | 004  | 1   | Editorial cleanup and completion of annexes in TS 36.111               | 11.2.0 | 11.3.0 |
| 09-2014        | RP-65 | RP-141530 | 0005 | 1   | Addition of Channel Bandwidth Section in TS 36.111                     | 11.3.0 | 11.4.0 |