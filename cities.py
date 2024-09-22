cities = [
    {"name": "Tel Aviv", "lat": 32.08088, "lon": 34.78057},
    {"name": "Shanghai", "lat": 31.230391, "lon": 121.473701},
    {"name": "São Paulo", "lat": -23.550520, "lon": -46.633308},
    {"name": "Bucharest", "lat": 44.426767, "lon": 26.102538},
    {"name": "Brisbane", "lat": -27.469770, "lon": 153.025131},
    {"name": "Larnaca", "lat": 34.923096, "lon": 33.634045},
    {'name': 'Columbus', 'lat': 39.9612, 'lon': -82.9988},
    {'name': 'Noumea', 'lat': -22.2558, 'lon': 166.4505},
    {'name': 'Tbilisi', 'lat': 41.7151, 'lon': 44.8271},
    {'name': 'Houston', 'lat': 29.7604, 'lon': -95.3698},
    {'name': 'Riga', 'lat': 56.9496, 'lon': 24.1052},
    {'name': 'San Juan', 'lat': 18.4655, 'lon': -66.1057},
    {'name': 'Asuncion', 'lat': -25.2637, 'lon': -57.5759},
    {'name': 'Belize City', 'lat': 17.5046, 'lon': -88.1962},
    {'name': 'Las Vegas', 'lat': 36.1699, 'lon': -115.1398},
    {'name': 'Kabul', 'lat': 34.5553, 'lon': 69.2075},
    {'name': 'Manila', 'lat': 14.5995, 'lon': 120.9842},
    {'name': 'Omsk', 'lat': 54.9914, 'lon': 73.3645},
    {'name': 'Dallas', 'lat': 32.7767, 'lon': -96.797},
    {'name': 'Lisbon', 'lat': 38.7223, 'lon': -9.1393},
    {'name': 'Kyoto', 'lat': 35.0116, 'lon': 135.7681},
    {'name': 'Tripoli', 'lat': 32.8872, 'lon': 13.1913},
    {'name': 'Nairobi', 'lat': -1.2921, 'lon': 36.8219},
    {'name': 'Sucre', 'lat': -19.0333, 'lon': -65.2627},
    {'name': 'Stockholm', 'lat': 59.3293, 'lon': 18.0686},
    {'name': 'Budapest', 'lat': 47.4979, 'lon': 19.0402},
    {'name': 'Indianapolis', 'lat': 39.7684, 'lon': -86.1581},
    {'name': 'Tehran', 'lat': 35.6892, 'lon': 51.389},
    {'name': 'Delhi', 'lat': 28.7041, 'lon': 77.1025},
    {'name': 'Sapporo', 'lat': 43.0618, 'lon': 141.3545},
    {'name': 'Pune', 'lat': 18.5204, 'lon': 73.8567},
    {'name': 'Libreville', 'lat': 0.4162, 'lon': 9.4673},
    {'name': 'Conakry', 'lat': 9.6412, 'lon': -13.5784},
    {'name': 'Atlanta', 'lat': 33.749, 'lon': -84.388},
    {'name': 'Kochi', 'lat': 9.9312, 'lon': 76.2673},
    {'name': 'Tokyo', 'lat': 35.6762, 'lon': 139.6503},
    {'name': 'Tromsø', 'lat': 69.6492, 'lon': 18.956},
    {'name': 'Chengdu', 'lat': 30.5728, 'lon': 104.0668},
    {'name': 'Gaborone', 'lat': -24.6282, 'lon': 25.9231},
    {'name': 'San Jose', 'lat': 9.9281, 'lon': -84.0907},
    {'name': 'Ouagadougou', 'lat': 12.3714, 'lon': -1.5197},
    {'name': 'Bissau', 'lat': 11.8817, 'lon': -15.6175},
    {'name': 'Tallinn', 'lat': 59.437, 'lon': 24.7536},
    {'name': 'Nassau', 'lat': 25.0343, 'lon': -77.3963},
    {'name': 'Johannesburg', 'lat': -26.2041, 'lon': 28.0473},
    {'name': 'Cancún', 'lat': 21.1619, 'lon': -86.8515},
    {'name': 'Copenhagen', 'lat': 55.6761, 'lon': 12.5683},
    {'name': 'Nagpur', 'lat': 21.1458, 'lon': 79.0882},
    {'name': 'Belo Horizonte', 'lat': -19.9167, 'lon': -43.9345},
    {'name': 'Cebu City', 'lat': 10.3157, 'lon': 123.8854},
    {'name': 'Malabo', 'lat': 3.7507, 'lon': 8.7837},
    {'name': 'Rosario', 'lat': -32.9442, 'lon': -60.6505},
    {'name': 'Casablanca', 'lat': 33.5731, 'lon': -7.5898},
    {'name': 'Lima', 'lat': -12.0464, 'lon': -77.0428},
    {'name': 'Auckland', 'lat': -36.8485, 'lon': 174.7633},
    {'name': 'Beijing', 'lat': 39.9042, 'lon': 116.4074},
    {'name': 'Moscow', 'lat': 55.7558, 'lon': 37.6173},
    {'name': 'Guatemala City', 'lat': 14.6349, 'lon': -90.5069},
    {'name': 'Sydney', 'lat': -33.8688, 'lon': 151.2093},
    {'name': 'San Francisco', 'lat': 37.7749, 'lon': -122.4194},
    {'name': 'Yekaterinburg', 'lat': 56.8389, 'lon': 60.6057},
    {'name': 'Chennai', 'lat': 13.0827, 'lon': 80.2707},
    {'name': 'Ho Chi Minh City', 'lat': 10.8231, 'lon': 106.6297},
    {'name': 'Osaka', 'lat': 34.6937, 'lon': 135.5023},
    {'name': 'Warsaw', 'lat': 52.2297, 'lon': 21.0122},
    {'name': 'San Pedro Sula', 'lat': 15.5042, 'lon': -88.025},
    {'name': "Xi'an", 'lat': 34.3416, 'lon': 108.9398},
    {'name': 'Windhoek', 'lat': -22.5595, 'lon': 17.0832},
    {'name': 'Salvador', 'lat': -12.9777, 'lon': -38.5016},
    {'name': 'Ottawa', 'lat': 45.4215, 'lon': -75.6972},
    {'name': 'Cairo', 'lat': 30.0444, 'lon': 31.2357},
    {'name': 'Bangkok', 'lat': 13.7563, 'lon': 100.5018},
    {'name': 'Zagreb', 'lat': 45.815, 'lon': 15.9819},
    {'name': 'Maputo', 'lat': -25.9655, 'lon': 32.5832},
    {'name': 'San Diego', 'lat': 32.7157, 'lon': -117.1611},
    {'name': 'Minsk', 'lat': 53.9006, 'lon': 27.559},
    {'name': 'Murmansk', 'lat': 68.9585, 'lon': 33.0827},
    {'name': 'Fukuoka', 'lat': 33.5904, 'lon': 130.4017},
    {'name': 'Caracas', 'lat': 10.4806, 'lon': -66.9036},
    {'name': 'Bamako', 'lat': 12.6392, 'lon': -8.0029},
    {'name': 'Fortaleza', 'lat': -3.7172, 'lon': -38.5434},
    {'name': 'Recife', 'lat': -8.0476, 'lon': -34.877},
    {'name': 'Seoul', 'lat': 37.5665, 'lon': 126.978},
    {'name': 'Philadelphia', 'lat': 39.9526, 'lon': -75.1652},
    {'name': 'Athens', 'lat': 37.9838, 'lon': 23.7275},
    {'name': 'Kigali', 'lat': -1.9706, 'lon': 30.1044},
    {'name': 'Jinan', 'lat': 36.6512, 'lon': 117.1201},
    {'name': 'Kathmandu', 'lat': 27.7172, 'lon': 85.324},
    {'name': 'Wuhan', 'lat': 30.5928, 'lon': 114.3055},
    {'name': 'Brussels', 'lat': 50.8503, 'lon': 4.3517},
    {'name': 'Bishkek', 'lat': 42.8746, 'lon': 74.5698},
    {'name': 'San Jose', 'lat': 37.3382, 'lon': -121.8863},
    {'name': 'Seattle', 'lat': 47.6062, 'lon': -122.3321},
    {'name': 'Bridgetown', 'lat': 13.0962, 'lon': -59.6147},
    {'name': 'Santiago', 'lat': -33.4489, 'lon': -70.6693},
    {'name': 'Quebec City', 'lat': 46.8139, 'lon': -71.2082},
    {'name': 'Berlin', 'lat': 52.52, 'lon': 13.405},
    {'name': 'Jakarta', 'lat': -6.2088, 'lon': 106.8456},
    {'name': 'Anchorage', 'lat': 61.2181, 'lon': -149.9003},
    {'name': 'Brasília', 'lat': -15.7942, 'lon': -47.8825},
    {'name': 'Ulsan', 'lat': 35.5384, 'lon': 129.3114},
    {'name': 'Guayaquil', 'lat': -2.1709, 'lon': -79.9224},
    {'name': 'Mérida', 'lat': 20.9674, 'lon': -89.5926},
    {'name': 'San Antonio', 'lat': 29.4241, 'lon': -98.4936},
    {'name': 'Baghdad', 'lat': 33.3152, 'lon': 44.3661},
    {'name': 'Tegucigalpa', 'lat': 14.0723, 'lon': -87.1921},
    {'name': 'Xiamen', 'lat': 24.4798, 'lon': 118.0895},
    {'name': 'Phoenix', 'lat': 33.4484, 'lon': -112.074},
    {'name': 'Portland', 'lat': 45.5155, 'lon': -122.6793},
    {'name': 'Accra', 'lat': 5.6037, 'lon': -0.187},
    {'name': 'Incheon', 'lat': 37.4563, 'lon': 126.7052},
    {'name': 'Calgary', 'lat': 51.0447, 'lon': -114.0719},
    {'name': 'Ufa', 'lat': 54.7388, 'lon': 55.9721},
    {'name': 'Changsha', 'lat': 28.2282, 'lon': 112.9388},
    {'name': 'Surat', 'lat': 21.1702, 'lon': 72.8311},
    {'name': 'Monrovia', 'lat': 6.3156, 'lon': -10.8074},
    {'name': 'Islamabad', 'lat': 33.6844, 'lon': 73.0479},
    {'name': 'Hyderabad', 'lat': 17.385, 'lon': 78.4867},
    {'name': 'Kingston', 'lat': 18.0179, 'lon': -76.8099},
    {'name': 'Djibouti', 'lat': 11.8251, 'lon': 42.5903},
    {'name': 'Amman', 'lat': 31.9539, 'lon': 35.9106},
    {'name': 'Douala', 'lat': 4.0511, 'lon': 9.7679},
    {'name': 'Port of Spain', 'lat': 10.6918, 'lon': -61.2225},
    {'name': 'Damascus', 'lat': 33.5138, 'lon': 36.2765},
    {'name': 'Nanjing', 'lat': 32.0603, 'lon': 118.7969},
    {'name': 'Jacksonville', 'lat': 30.3322, 'lon': -81.6557},
    {'name': 'Charlotte', 'lat': 35.2271, 'lon': -80.8431},
    {'name': 'Yamoussoukro', 'lat': 6.8276, 'lon': -5.2893},
    {'name': 'Cartagena', 'lat': 10.391, 'lon': -75.4794},
    {'name': 'Havana', 'lat': 23.1136, 'lon': -82.3666},
    {'name': 'Managua', 'lat': 12.115, 'lon': -86.2362},
    {'name': 'Monterrey', 'lat': 25.6866, 'lon': -100.3161},
    {'name': 'Irkutsk', 'lat': 52.2869, 'lon': 104.305},
    {'name': 'Mumbai', 'lat': 19.076, 'lon': 72.8777},
    {'name': 'Santo Domingo', 'lat': 18.4861, 'lon': -69.9312},
    {'name': 'Dushanbe', 'lat': 38.5598, 'lon': 68.787},
    {'name': 'Lagos', 'lat': 6.5244, 'lon': 3.3792},
    {'name': 'Tashkent', 'lat': 41.2995, 'lon': 69.2401},
    {'name': 'Cape Town', 'lat': -33.9249, 'lon': 18.4241},
    {'name': 'Luanda', 'lat': -8.839, 'lon': 13.2894},
    {'name': 'Colombo', 'lat': 6.9271, 'lon': 79.8612},
    {'name': 'Shenzhen', 'lat': 22.5431, 'lon': 114.0579},
    {'name': 'Bujumbura', 'lat': -3.3731, 'lon': 29.9189},
    {'name': 'Asunción', 'lat': -25.2637, 'lon': -57.5759},
    {'name': 'Cotonou', 'lat': 6.3654, 'lon': 2.4183},
    {'name': 'Skopje', 'lat': 41.9981, 'lon': 21.4254},
    {'name': 'Vancouver', 'lat': 49.2827, 'lon': -123.1207},
    {'name': 'Oslo', 'lat': 59.9139, 'lon': 10.7522},
    {'name': 'Lhasa', 'lat': 29.6456, 'lon': 91.1409},
    {'name': 'Winnipeg', 'lat': 49.8951, 'lon': -97.1384},
    {'name': 'Antananarivo', 'lat': -18.8792, 'lon': 47.5079},
    {'name': 'Ashgabat', 'lat': 37.9601, 'lon': 58.3261},
    {'name': 'Da Nang', 'lat': 16.0544, 'lon': 108.2022},
    {'name': 'Harbin', 'lat': 45.8038, 'lon': 126.5349},
    {'name': 'Bangalore', 'lat': 12.9716, 'lon': 77.5946},
    {'name': 'Zhengzhou', 'lat': 34.7466, 'lon': 113.6254},
    {'name': 'Rome', 'lat': 41.9028, 'lon': 12.4964},
    {'name': 'Lusaka', 'lat': -15.3875, 'lon': 28.3228},
    {'name': 'Bergen', 'lat': 60.3913, 'lon': 5.3221},
    {'name': 'Kyiv', 'lat': 50.4501, 'lon': 30.5234},
    {'name': 'Vladivostok', 'lat': 43.1155, 'lon': 131.8855},
    {'name': 'Toronto', 'lat': 43.6511, 'lon': -79.3837},
    {'name': 'Nashville', 'lat': 36.1627, 'lon': -86.7816},
    {'name': 'Madrid', 'lat': 40.4168, 'lon': -3.7038},
    {'name': 'Suva', 'lat': -18.1416, 'lon': 178.4419},
    {'name': 'Los Angeles', 'lat': 34.0522, 'lon': -118.2437},
    {'name': 'Sarajevo', 'lat': 43.8563, 'lon': 18.4131},
    {'name': 'Malmo', 'lat': 55.605, 'lon': 13.0038},
    {'name': 'Medellín', 'lat': 6.2442, 'lon': -75.5812},
    {'name': 'Guadalajara', 'lat': 20.6597, 'lon': -103.3496},
    {'name': 'Honolulu', 'lat': 21.3069, 'lon': -157.8583},
    {'name': 'Ulaanbaatar', 'lat': 47.8864, 'lon': 106.9057},
    {'name': 'Abu Dhabi', 'lat': 24.4539, 'lon': 54.3773},
    {'name': 'Nouakchott', 'lat': 18.0735, 'lon': -15.9582},
    {'name': 'Mombasa', 'lat': -4.0435, 'lon': 39.6682},
    {'name': 'Washington, D.C.', 'lat': 38.9072, 'lon': -77.0369},
    {'name': 'Vienna', 'lat': 48.2082, 'lon': 16.3738},
    {'name': 'Montevideo', 'lat': -34.9011, 'lon': -56.1645},
    {'name': 'Thimphu', 'lat': 27.4712, 'lon': 89.6369},
    {'name': 'León', 'lat': 21.1236, 'lon': -101.6844},
    {'name': 'Vilnius', 'lat': 54.6872, 'lon': 25.2797},
    {'name': 'Córdoba', 'lat': -31.4201, 'lon': -64.1888},
    {'name': 'Mexico City', 'lat': 19.4326, 'lon': -99.1332},
    {'name': 'Nagoya', 'lat': 35.1815, 'lon': 136.9066},
    {'name': 'Bhopal', 'lat': 23.2599, 'lon': 77.4126},
    {'name': 'Algiers', 'lat': 36.7372, 'lon': 3.0865},
    {'name': 'Panama City', 'lat': 8.9833, 'lon': -79.5199},
    {'name': 'Halifax', 'lat': 44.6488, 'lon': -63.5752},
    {'name': 'Cusco', 'lat': -13.5319, 'lon': -71.9675},
    {'name': 'Boston', 'lat': 42.3601, 'lon': -71.0589},
    {'name': 'Niamey', 'lat': 13.5126, 'lon': 2.1128},
    {'name': 'Paris', 'lat': 48.8566, 'lon': 2.3522},
    {'name': 'Ahmedabad', 'lat': 23.0225, 'lon': 72.5714},
    {'name': 'Buenos Aires', 'lat': -34.6037, 'lon': -58.3816},
    {'name': 'Manaus', 'lat': -3.119, 'lon': -60.0217},
    {'name': 'Denver', 'lat': 39.7392, 'lon': -104.9903},
    {'name': 'Singapore', 'lat': 1.3521, 'lon': 103.8198},
    {'name': 'Krasnoyarsk', 'lat': 56.0153, 'lon': 92.8932},
    {'name': 'Shenyang', 'lat': 41.8057, 'lon': 123.4315},
    {'name': 'Addis Ababa', 'lat': 9.145, 'lon': 38.7636},
    {'name': 'Montreal', 'lat': 45.5017, 'lon': -73.5673},
    {'name': 'Dubai', 'lat': 25.276, 'lon': 55.2962},
    {'name': 'Port Moresby', 'lat': -9.4438, 'lon': 147.1803},
    {'name': 'Blantyre', 'lat': -15.7861, 'lon': 35.0058},
    {'name': 'Harare', 'lat': -17.8292, 'lon': 31.0522},
    {'name': 'Manama', 'lat': 26.2285, 'lon': 50.586},
    {'name': 'Hangzhou', 'lat': 30.2741, 'lon': 120.1551},
    {'name': 'London', 'lat': 51.5074, 'lon': -0.1278},
    {'name': 'Daegu', 'lat': 35.8722, 'lon': 128.6025},
    {'name': 'Prague', 'lat': 50.0755, 'lon': 14.4378},
    {'name': 'Abidjan', 'lat': 5.36, 'lon': -4.0083},
    {'name': 'Jaipur', 'lat': 26.9124, 'lon': 75.7873},
    {'name': 'New Orleans', 'lat': 29.9511, 'lon': -90.0715},
    {'name': 'Istanbul', 'lat': 41.0082, 'lon': 28.9784},
    {'name': 'Vientiane', 'lat': 17.9757, 'lon': 102.6331},
    {'name': 'Miami', 'lat': 25.7617, 'lon': -80.1918},
    {'name': 'Edmonton', 'lat': 53.5461, 'lon': -113.4938},
    {'name': 'Davao City', 'lat': 7.1907, 'lon': 125.4553},
    {'name': 'Melbourne', 'lat': -37.8136, 'lon': 144.9631},
    {'name': 'Lome', 'lat': 6.1725, 'lon': 1.2314},
    {'name': 'Bogotá', 'lat': 4.711, 'lon': -74.0721},
    {'name': 'Dakar', 'lat': 14.6928, 'lon': -17.4467},
    {'name': 'Muscat', 'lat': 23.588, 'lon': 58.3829},
    {'name': 'Tunis', 'lat': 36.8065, 'lon': 10.1815},
    {'name': 'Saint Petersburg', 'lat': 59.9343, 'lon': 30.3351},
    {'name': 'Rio de Janeiro', 'lat': -22.9068, 'lon': -43.1729},
    {'name': 'La Paz', 'lat': -16.5, 'lon': -68.15},
    {'name': 'Doha', 'lat': 25.276, 'lon': 51.5222},
    {'name': 'Stavanger', 'lat': 58.969, 'lon': 5.7331},
    {'name': 'Sendai', 'lat': 38.2682, 'lon': 140.8694},
    {'name': 'Sofia', 'lat': 42.6977, 'lon': 23.3219},
    {'name': 'Kuala Lumpur', 'lat': 3.139, 'lon': 101.6869},
    {'name': 'Kuwait City', 'lat': 29.3759, 'lon': 47.9774},
    {'name': 'Cali', 'lat': 3.4516, 'lon': -76.532},
    {'name': 'Hanoi', 'lat': 21.0285, 'lon': 105.8542},
    {'name': 'Helsinki', 'lat': 60.1695, 'lon': 24.9355},
    {'name': 'New York', 'lat': 40.7128, 'lon': -74.006},
    {'name': 'Gothenburg', 'lat': 57.7089, 'lon': 11.9746},
    {'name': 'Yaoundé', 'lat': 3.848, 'lon': 11.5021},
    {'name': 'Novosibirsk', 'lat': 55.0084, 'lon': 82.9357},
    {'name': 'Beirut', 'lat': 33.8938, 'lon': 35.5018},
    {'name': 'Apia', 'lat': -13.8507, 'lon': -171.7514},
    {'name': 'Reykjavik', 'lat': 64.1466, 'lon': -21.9426},
    {'name': 'Busan', 'lat': 35.1796, 'lon': 129.0756},
    {'name': 'Chicago', 'lat': 41.8781, 'lon': -87.6298},
    {'name': 'Memphis', 'lat': 35.1495, 'lon': -90.049},
    {'name': 'Banjul', 'lat': 13.4549, 'lon': -16.579},
    {'name': 'Port-au-Prince', 'lat': 18.5944, 'lon': -72.3074},
    {'name': 'Santa Cruz de la Sierra', 'lat': -17.7833, 'lon': -63.1821},
    {'name': 'Quito', 'lat': -0.1807, 'lon': -78.4678},
    {'name': 'San Salvador', 'lat': 13.6929, 'lon': -89.2182},
    {'name': 'Kinshasa', 'lat': -4.4419, 'lon': 15.2663},
    {'name': 'Freetown', 'lat': 8.4657, 'lon': -13.2317},
    {'name': 'Tijuana', 'lat': 32.5149, 'lon': -117.0382},
    {"name": "Birmingham", "lat": 52.486244, "lon": -1.890401},
    {"name": "Manchester", "lat": 53.483959, "lon": -2.244644},
    {"name": "Edinburgh", "lat": 55.953251, "lon": -3.188267},
    {"name": "Dublin", "lat": 53.349805, "lon": -6.26031},
    {"name": "Marseille", "lat": 43.296482, "lon": 5.36978},
    {"name": "Munich", "lat": 48.135125, "lon": 11.581981},
    {"name": "Zurich", "lat": 47.376886, "lon": 8.541694},
    {"name": "Milan", "lat": 45.464204, "lon": 9.189982},
    {"name": "Palermo", "lat": 38.11569, "lon": 13.361486},
    {"name": "Valletta", "lat": 35.89972, "lon": 14.514722},
    {"name": "Sassari", "lat": 40.727503, "lon": 8.559373},
    {"name": "Palma", "lat": 39.5696, "lon": 2.65016},
    {"name": "Barcelona", "lat": 41.385064, "lon": 2.173404},
    {"name": "Valencia", "lat": 39.469907, "lon": -0.376288},
    {"name": "Sevilla", "lat": 37.389092, "lon": -5.984459},
    {"name": "Bangui", "lat": 4.394674, "lon": 18.55819},
    {"name": "Kisangani", "lat": 0.51528, "lon": 25.19158},
    {"name": "Dar es Salaam", "lat": -6.792354, "lon": 39.208328},
    {"name": "Funchal", "lat": 32.666867, "lon": -16.924055},
    {"name": "Las Palmas", "lat": 28.123546, "lon": -15.436257},
    {"name": "Antalya", "lat": 36.896891, "lon": 30.713323},
    {"name": "Aleppo", "lat": 36.202105, "lon": 37.134259},
    {"name": "Mosul", "lat": 36.3308, "lon": 43.1056},
    {"name": "Yerevan", "lat": 40.179188, "lon": 44.499104},
    {"name": "Baku", "lat": 40.409262, "lon": 49.867092},
    {"name": "Volgograd", "lat": 48.708048, "lon": 44.513303},
    {"name": "Vorkuta", "lat": 67.498842, "lon": 64.052478},
    {"name": "Olenek", "lat": 68.514444, "lon": 112.440556},
    {"name": "Kansas City", "lat": 39.099727, "lon": -94.578567},
    {"name": "Oklahoma City", "lat": 35.46756, "lon": -97.516428},
    {"name": "Chihuahua", "lat": 28.632996, "lon": -106.0691},
    {"name": "Stanley", "lat": -51.697709, "lon": -57.851662},
    {"name": "Luxor", "lat": 25.687243, "lon": 32.639637},
    {"name": "Khartoum", "lat": 15.500654, "lon": 32.559899},
    {"name": "Huambo", "lat": -12.77611, "lon": 15.734618},
    {"name": "At Taj", "lat": 24.199138, "lon": 23.290087},
    {"name": "Mecca", "lat": 21.42251, "lon": 39.826168},
    {"name": "Sanaa", "lat": 15.369445, "lon": 44.191007},
    {"name": "Kuching", "lat": 1.553533, "lon": 110.35928},
    {"name": "Palu", "lat": -0.901159, "lon": 119.870703},
    {"name": "Dili", "lat": -8.558625, "lon": 125.57361},
    {"name": "Darwin", "lat": -12.46344, "lon": 130.845642},
    {"name": "Alice Springs", "lat": -23.698042, "lon": 133.880747},
    {"name": "Adelaide", "lat": -34.928497, "lon": 138.600741},
    {"name": "Hobart", "lat": -42.882138, "lon": 147.327195},
    {"name": "Apia", "lat": -13.83333, "lon": -171.76666},
    {"name": "Astana", "lat": 51.169392, "lon": 71.449074},
    {"name": "Inverness", "lat": 57.477772, "lon": -4.224721},
    {"name": "Stromness", "lat": 58.964122, "lon": -3.296256},
    {"name": "Lerwick", "lat": 60.155141, "lon": -1.145690},
    {"name": "Torshavn", "lat": 62.007864, "lon": -6.790982},
    {"name": "Umea", "lat": 63.825847, "lon": 20.263035},
    {"name": "Bodo", "lat": 67.280356, "lon": 14.404917},
    {"name": "Trondheim", "lat": 63.430515, "lon": 10.395053},
    {"name": "Oulu", "lat": 65.012093, "lon": 25.465077},
    {"name": "Kirov", "lat": 58.603572, "lon": 49.668378},
    {"name": "Ukhta", "lat": 63.567051, "lon": 53.684029},
    {"name": "Nadym", "lat": 65.533747, "lon": 72.516611},
    {"name": "Surgut", "lat": 61.253248, "lon": 73.396221},
    {"name": "Lesosibirsk", "lat": 58.221103, "lon": 92.482121},
    {"name": "Yakutsk", "lat": 62.035452, "lon": 129.675475},
    {"name": "Hotan", "lat": 37.107536, "lon": 79.935435},
    {"name": "Liuyuan", "lat": 42.724763, "lon": 93.327913},
    {"name": "Urumqi", "lat": 43.825592, "lon": 87.616848},
    {"name": "Altay", "lat": 47.845289, "lon": 88.133006},
    {"name": "Jezkazgan", "lat": 47.787731, "lon": 67.707955},
    {"name": "Balqash", "lat": 46.85307, "lon": 74.950568},
    {"name": "Almaty", "lat": 43.222015, "lon": 76.851248},
    {"name": "Nukus", "lat": 42.453063, "lon": 59.607029},
    {"name": "Zahedan", "lat": 29.4963, "lon": 60.8629},
    {"name": "Bandar Abbas", "lat": 27.192078, "lon": 56.275699},
    {"name": "Shiraz", "lat": 29.591768, "lon": 52.583698},
    {"name": "Tabriz", "lat": 38.070033, "lon": 46.301282},
    {"name": "Batman", "lat": 37.881168, "lon": 41.13509},
    {"name": "Adana", "lat": 37.0, "lon": 35.321333},
    {"name": "Ankara", "lat": 39.933365, "lon": 32.859741},
    {"name": "Trabzon", "lat": 41.00145, "lon": 39.7178},
    {"name": "Krasnodar", "lat": 45.03547, "lon": 38.975313},
    {"name": "Donetsk", "lat": 48.015883, "lon": 37.80285},
    {"name": "Odesa", "lat": 46.482526, "lon": 30.723309},
    {"name": "Sevastopol", "lat": 44.61665, "lon": 33.525367},
    {"name": "Chisinau", "lat": 47.010452, "lon": 28.86381},
    {"name": "Kharkiv", "lat": 49.9935, "lon": 36.2304},
    {"name": "Lviv", "lat": 49.839683, "lon": 24.029717},
    {"name": "Bratislava", "lat": 48.148596, "lon": 17.107748},
    {"name": "Debrecen", "lat": 47.531605, "lon": 21.627312},
    {"name": "Kosice", "lat": 48.716385, "lon": 21.261074},
    {"name": "Krakow", "lat": 50.064651, "lon": 19.944981},
    {"name": "Poznan", "lat": 52.406376, "lon": 16.925167},
    {"name": "Wroclaw", "lat": 51.107883, "lon": 17.038538},
    {"name": "Lodz", "lat": 51.759248, "lon": 19.455983},
    {"name": "Gdansk", "lat": 54.352025, "lon": 18.646638},
    {"name": "Tartu", "lat": 58.377625, "lon": 26.729006},
    {"name": "Plymouth", "lat": 50.375456, "lon": -4.142656},
    {"name": "Cork", "lat": 51.898514, "lon": -8.475604},
    {"name": "Galway", "lat": 53.270668, "lon": -9.056791},
    {"name": "Belfast", "lat": 54.597285, "lon": -5.93012},
    {"name": "Bordeaux", "lat": 44.837789, "lon": -0.57918},
    {"name": "Nantes", "lat": 47.218371, "lon": -1.553621},
    {"name": "Brest", "lat": 48.390394, "lon": -4.486076},
    {"name": "Lorient", "lat": 47.750839, "lon": -3.366586},
    {"name": "Lyon", "lat": 45.764043, "lon": 4.835659},
    {"name": "Stuttgart", "lat": 48.775846, "lon": 9.182932},
    {"name": "Frankfurt", "lat": 50.110924, "lon": 8.682127},
    {"name": "Cologne", "lat": 50.937531, "lon": 6.960279},
    {"name": "Bremen", "lat": 53.079296, "lon": 8.801694},
    {"name": "Amsterdam", "lat": 52.367573, "lon": 4.904139},
    {"name": "Rotterdam", "lat": 51.9225, "lon": 4.47917},
    {"name": "Dresden", "lat": 51.050407, "lon": 13.737262},
    {"name": "Ostrava", "lat": 49.820922, "lon": 18.262524},
    {"name": "Monaco", "lat": 43.738418, "lon": 7.424616},
    {"name": "Zaragoza", "lat": 41.648823, "lon": -0.889085},
    {"name": "Malaga", "lat": 36.721273, "lon": -4.421399},
    {"name": "Marbella", "lat": 36.510072, "lon": -4.882447},
    {"name": "Rabat", "lat": 34.020882, "lon": -6.84165},
    {"name": "Agadir", "lat": 30.427755, "lon": -9.598108},
    {"name": "Zagora", "lat": 30.348738, "lon": -5.839708},
    {"name": "Atar", "lat": 20.51775, "lon": -13.05201},
    {"name": "Douentza", "lat": 15.00693, "lon": -2.9496},
    {"name": "Djibo", "lat": 14.0994, "lon": -1.62656},
    {"name": "Banfora", "lat": 10.63054, "lon": -4.75821},
    {"name": "Tamale", "lat": 9.40079, "lon": -0.8393},
    {"name": "Badou", "lat": 7.583333, "lon": 0.6},
    {"name": "Lama-Kara", "lat": 9.55111, "lon": 1.18611},
    {"name": "Tcharourou", "lat": 8.883333, "lon": 2.6},
    {"name": "Oshogbo", "lat": 7.773837, "lon": 4.556978},
    {"name": "Benin City", "lat": 6.334987, "lon": 5.603276},
    {"name": "Onitsha", "lat": 6.144126, "lon": 6.785282},
    {"name": "Kaduna", "lat": 10.52641, "lon": 7.43879},
    {"name": "Sarh", "lat": 9.1448, "lon": 18.3743},
    {"name": "Al Junaynah", "lat": 13.45, "lon": 22.46667},
    {"name": "An Nuhud", "lat": 12.7, "lon": 28.417},
    {"name": "Asmara", "lat": 15.322877, "lon": 38.925052},
    {"name": "Hargeisa", "lat": 9.562389, "lon": 44.077013},
    {"name": "Mogadishu", "lat": 2.046934, "lon": 45.318162},
    {"name": "Wajir", "lat": 1.74876, "lon": 40.05732},
    {"name": "Lodwar", "lat": 3.11913, "lon": 35.59728},
    {"name": "Dodoma", "lat": -6.1630, "lon": 35.7516},
    {"name": "Lilongwe", "lat": -13.9626, "lon": 33.7741},
    {"name": "Lubumbashi", "lat": -11.6877, "lon": 27.4794},
    {"name": "Ghanzi", "lat": -21.56667, "lon": 21.78333},
    {"name": "Calvinia", "lat": -31.47, "lon": 19.776},
    {"name": "Saldanha", "lat": -33.0117, "lon": 17.9448},
    {"name": "Port Elizabeth", "lat": -33.9611, "lon": 25.6149},
    {"name": "East London", "lat": -33.0292, "lon": 27.8546},
    {"name": "Maseru", "lat": -29.3151, "lon": 27.4869},
    {"name": "Bloemfontein", "lat": -29.0852, "lon": 26.1596},
    {"name": "Durban", "lat": -29.8579, "lon": 31.0292},
    {"name": "Lombamba", "lat": -26.4667, "lon": 31.2},
    {"name": "Baira", "lat": -19.82533, "lon": 34.87803},
    {"name": "Angoche", "lat": -16.23250, "lon": 39.90861},
    {"name": "Karachi", "lat": 24.860735, "lon": 67.001137},
    {"name": "Hyderabad", "lat": 25.396, "lon": 68.3737},
    {"name": "Lahore", "lat": 31.5497, "lon": 74.3436},
    {"name": "Kolkata", "lat": 22.5726, "lon": 88.3639},
    {"name": "Dhaka", "lat": 23.8103, "lon": 90.4125},
    {"name": "Yangon", "lat": 16.8409, "lon": 96.1735},
    {"name": "Nay Pyi Taw", "lat": 19.7633, "lon": 96.0785},
    {"name": "Phnom Penh", "lat": 11.5564, "lon": 104.9282},
    {"name": "Taipei", "lat": 25.03396, "lon": 121.56447},
    {"name": "Tainan", "lat": 22.99973, "lon": 120.22703},
    {"name": "Wenzhou", "lat": 27.993828, "lon": 120.699363},
    {"name": "Pyongyang", "lat": 39.0392, "lon": 125.7625},
    {"name": "Perth", "lat": -31.950527, "lon": 115.860457},
    {"name": "Christchurch", "lat": -43.5321, "lon": 172.6362},
    {"name": "Bari", "lat": 41.117143, "lon": 16.871871},
    {"name": "Tirana", "lat": 41.3275, "lon": 19.8189},
    {"name": "Podgorica", "lat": 42.43042, "lon": 19.25936},
    {"name": "Prishtina", "lat": 42.6629, "lon": 21.1655},
    {"name": "Thessaloniki", "lat": 40.640063, "lon": 22.944419},
    {"name": "Zakinthos", "lat": 37.787, "lon": 20.8994},
    {"name": "Iraklio", "lat": 35.3387, "lon": 25.1442},
    {"name": "Hania", "lat": 35.5138, "lon": 24.018},
    {"name": "Rhodes", "lat": 36.434, "lon": 28.217},
    {"name": "Izmir", "lat": 38.4237, "lon": 27.1428},
    {"name": "Bursa", "lat": 40.1828, "lon": 29.0663},
    {"name": "Varna", "lat": 43.214, "lon": 27.9147},
    {"name": "Iasi", "lat": 47.1585, "lon": 27.6014},
    {"name": "Riyadh", "lat": 24.7136, "lon": 46.6753},
    {"name": "Arlit", "lat": 18.7369, "lon": 7.3853},
    {"name": "Tamanrasset", "lat": 22.785, "lon": 5.5228},
    {"name": "Marrakech", "lat": 31.6295, "lon": -7.9811},
    {"name": "Marzuq", "lat": 25.914, "lon": 13.918},
    {"name": "Waddan", "lat": 29.1603, "lon": 16.1385},
    {"name": "Banghazi", "lat": 32.1167, "lon": 20.0667},
    {"name": "Aswan", "lat": 24.0889, "lon": 32.8998},
    {"name": "Medina", "lat": 24.5247, "lon": 39.5692},
    {"name": "El Paso", "lat": 31.7619, "lon": -106.4850},
    {"name": "Salt Lake City", "lat": 40.7608, "lon": -111.8910},
    {"name": "Minneapolis", "lat": 44.9778, "lon": -93.2650},
    {"name": "Detroit", "lat": 42.3314, "lon": -83.0458},
    {"name": "Milwaukee", "lat": 43.0389, "lon": -87.9065},
    {"name": "Belém", "lat": -1.4550, "lon": -48.5040},
    {"name": "Campo Grande", "lat": -20.4697, "lon": -54.6201},
    {"name": "Río Gallegos", "lat": -51.6230, "lon": -69.2168},
    {"name": "Canberra", "lat": -35.2809, "lon": 149.1300},
    {"name": "Cairns", "lat": -16.9203, "lon": 145.7710},
    {"name": "Honiara", "lat": -9.4456, "lon": 159.9729},
    {"name": "Bandar Seri Begawan", "lat": 4.9031, "lon": 114.9398},
    {"name": "Palembang", "lat": -2.9761, "lon": 104.7754}
]
