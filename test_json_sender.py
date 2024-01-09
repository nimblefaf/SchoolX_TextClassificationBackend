import requests

sample_text_math = '''We introduce and develop the notion of spherical polyharmonics, which are a
natural generalisation of spherical harmonics. In particular we study the
theory of zonal polyharmonics, which allows us, analogously to zonal harmonics,
to construct Poisson kernels for polyharmonic functions on the union of rotated
balls. We find the representation of Poisson kernels and zonal polyharmonics in
terms of the Gegenbauer polynomials. We show the connection between the
classical Poisson kernel for harmonic functions on the ball, Poisson kernels
for polyharmonic functions on the union of rotated balls, and the Cauchy-Hua
kernel for holomorphic functions on the Lie ball.'''

sample_text_geology = '''
Minerals are the basic naturally occurring inorganic homogeneous
units having definite physical and chemical properties which are combined in various ways and under different conditions to form rocks.
Most minerals consist of elements combined as chemical compounds although a few may occur as native elements, for example gold, silver, copper, and carbon (diamond and graphite).
Eight elements make up about 98% of the earth’s crust. Oxygen is
the most abundant and seven other elements unite with oxygen to
make up many of the common minerals. The most fundamental combination of these elements is their union with oxygen to form oxides. When silicon unites with oxygen, silicon dioxide is formed,
which unites with water and forms acids. The six other elements
unite with oxygen and water to form bases. The acids and bases
combine to form silicates, which are the most abundant compounds
in the earth’s crust.
Feldspars
Feldspars are probably more widely-distributed than any other
group of rock forming minerals. They occur in most of the igneous
rocks, such as granites and lavas; in certain sandstones and conglomerates among sedimentary ones; and in gneisses of the metamorphic
rocks.
Feldspar is a family name, and not that of a single mineral. It constitutes one of the most, if not the most, important group of rock-forming
minerals; nearly 45% of the earth’s crust is composed of feldspar.
Quartz
Quartz is one of the commonest minerals which is present in many
rocks and solids in a wide variety of forms. It consists of silicon and
oxygen. It forms the major proportion of most sands.
Quartz is crystalline, it possesses no cleavage, its colour varies
widely from colourless or white through grey and brown to black,
sometimes yellow, red, pink, green and blue. It is luster vitreous,
sometimes greasy. It is brittle.
Quartz has widespread occurrence in igneous, sedimentary and
metamorphic rocks. It is an important constituent of the acid igneous
rocks, such as granites, and may occur in gneisses, and is the predominant constituent in quatzites. It is common in sedimentary rocks,
forming the principle mineral in sandstones. It is associated in rocks
chiefly with feldspar.
'''

sample_text_geodesy = '''
Understanding Geodetic Methods for Earth's Shape and Size.
Geodesy, the scientific discipline dealing with Earth's shape and size, employs various methods to measure and define our planet. Trilateration, a key technique, involves measuring the angles and distances between a network of points. This method, alongside satellite observations and GPS technology, enables accurate mapping and geodetic computations.
The Impact of Satellite Geodesy on Modern Navigation.
Satellite geodesy has revolutionized navigation through the Global Positioning System (GPS). This technology relies on signals from satellites to determine precise locations on Earth's surface. Innovations like Differential GPS enhance accuracy by compensating for signal distortions caused by atmospheric conditions.
Geodetic Datums: Establishing a Spatial Reference Framework.
Geodetic datums, reference systems for spatial data, are critical for ensuring consistency in mapping and navigation. WGS84 and NAD83 are common datums used globally, providing a standardized foundation for geospatial information.
Monitoring Ground Deformation: A Geodetic Approach to Safety.
Geodetic techniques play a vital role in monitoring ground deformation, ensuring the stability of critical infrastructure. Continuous GPS observations and advanced tools like InSAR enable real-time tracking of land movements, contributing to hazard prevention.
Unlocking Earth's Mysteries: Gravity Measurements in Geodesy.
Geodesists employ gravity measurements to unravel Earth's gravitational field. Gravimetric surveys, utilizing precise instruments like gravimeters, map variations in gravity, contributing valuable insights for geological studies.
'''

sample_text_neftegas = '''
Introduction.
Natural gas, electricity, and oil are forms of energy that are of particular interest to the Federal Energy Regulatory Commission pursuant to its authority under the Natural Gas Act, the Federal Power Act, and the Interstate Commerce Act. This primer
explores the workings of the wholesale markets for these forms of energy, as well as energy-related financial markets.
Natural gas is the second largest primary source of energy
consumed in the United States, exceeded only by petroleum.
A primary energy source is an energy source that can be consumed directly or converted into something else, like electricity. Roughly a third of the natural gas consumed in the United
States goes into power plants for the production of electricity.
Electricity, a secondary energy source, results from the conversion of primary fuels such as fossil fuels, uranium, wind, or
solar into a flow of electrons used to power modern life.
Crude oil and petroleum products are of interest to the Commission because it regulates the transport of oil by pipelines in
interstate commerce.
Energy markets involve both physical and financial elements.
The physical markets contain the natural resources, infrastructure, institutions and market participants involved in producing energy and delivering it to consumers. They also include
the trading of and payment for the physical commodity - e.g.,
natural gas. The financial markets include the buying and selling of financial products derived from the physical energy.
These financial markets also include market structures and
institutions, market participants, products and trading, and
have their own drivers of supply and demand. In general, physical and financial markets can be distinguished by the products and by the intentions of the market participants involved.
Physical products are those whose contracts involve the
physical delivery of the energy. Physical market participants
are those who are in the market to make or take delivery of
the commodity. Financial products usually do not involve the
delivery of natural gas, electricity, or oil; instead, they involve
the exchange of money.
'''

# 'predict' or 'get_prob"
data = {'Action': 'get_prob',
        'Data': sample_text_geology}

tmp_data = {'text': sample_text_geodesy}

localhost = 'http://localhost:43560/'
remote = 'http://46.147.115.140:8080'

response = requests.post(remote, json=tmp_data)
print(response.text)