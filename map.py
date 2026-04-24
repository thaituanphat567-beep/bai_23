#Bai 1

import folium

ueh_coords = [10.7629, 106.6822]


m = folium.Map(
    location=ueh_coords,
    zoom_start=14,
    tiles="OpenStreetMap"
)

ueh_layer = folium.FeatureGroup(name="UEH")

folium.Marker(
    location=ueh_coords,
    popup="Đại học Kinh tế TP.HCM (UEH)",
    tooltip="UEH",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(ueh_layer)

ueh_layer.add_to(m)


nearby_layer = folium.FeatureGroup(name="Địa điểm lân cận")


folium.Marker(location=[10.7709, 106.6687], popup="Vạn Hạnh Mall", icon = folium.Icon(color ="green")).add_to(nearby_layer)
folium.Marker(location=[10.7625, 106.6779], popup="Bệnh viện Nhi Đồng 1", icon = folium.Icon(color ="green")).add_to(nearby_layer)
folium.Marker(location=[10.7738, 106.6608], popup="Trường Phổ thông Năng Khiếu", icon = folium.Icon(color ="green")).add_to(nearby_layer)
folium.Marker(location=[10.7668, 106.6705], popup="THPT Lê Hồng Phong", icon = folium.Icon(color ="green")).add_to(nearby_layer)
folium.Marker(location=[10.7587, 106.6649], popup="Đại học Y Dược - Phạm Ngọc Thạch", icon = folium.Icon(color ="green")).add_to(nearby_layer)

nearby_layer.add_to(m)

folium.LayerControl().add_to(m)

m

#Bai 2

# BÀI 23.2

import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

geolocator = Nominatim(user_agent="ueh_project")

center_address = "UEH University, Ho Chi Minh City, Vietnam"
center_location = geolocator.geocode(center_address)

ueh_coords = (
    center_location.latitude,
    center_location.longitude
)


m = folium.Map(
    location=ueh_coords,
    zoom_start=6,
    tiles="OpenStreetMap"
)

center_layer = folium.FeatureGroup(name="UEH")

folium.Marker(
    location=ueh_coords,
    popup="UEH - Điểm trung tâm",
    tooltip="UEH",
    icon=folium.Icon(color="red")
).add_to(center_layer)

center_layer.add_to(m)


addresses = [
    "Van Hanh Mall, Ho Chi Minh City, Vietnam",
    "Children Hospital 1, Ho Chi Minh City, Vietnam",
    "Le Hong Phong High School, Ho Chi Minh City, Vietnam",
    "Pham Ngoc Thach University of Medicine, Ho Chi Minh City, Vietnam",
    "Landmark 81, Ho Chi Minh City, Vietnam",

    "Hoan Kiem Lake, Hanoi, Vietnam",
    "Da Nang International Airport, Da Nang, Vietnam",
    "Imperial City Hue, Hue, Vietnam",
    "Nha Trang Beach, Khanh Hoa, Vietnam",
    "Can Tho University, Can Tho, Vietnam"
]

place_layer = folium.FeatureGroup(name="Các địa điểm")

for address in addresses:

    location = geolocator.geocode(address)

    if location:
        coords = (location.latitude, location.longitude)

        distance_km = geodesic(ueh_coords, coords).km

        folium.Marker(
            location=coords,
            popup=f"{address}<br>{distance_km:.2f} km",
            tooltip=address,
            icon=folium.Icon(color="green")
        ).add_to(place_layer)

        folium.PolyLine(
            [ueh_coords, coords],
            color="blue",
            weight=2
        ).add_to(m)

    time.sleep(1)

place_layer.add_to(m)

folium.LayerControl().add_to(m)

m

#Bai 3

import folium
import random
from folium.plugins import HeatMap

ueh_coords = [10.7629, 106.6822]


m = folium.Map(
    location=ueh_coords,
    zoom_start=13
)


heat_data = []

for i in range(100):
    ViDo = 10.7629 + random.uniform(-0.02, 0.02)
    KinhDo = 106.6822 + random.uniform(-0.02, 0.02)

    heat_data.append([ViDo, KinhDo])


HeatMap(heat_data).add_to(m)


folium.Marker(
    location=ueh_coords,
    popup="UEH",
    icon=folium.Icon(color="red")
).add_to(m)


m

#Bai 4

from google.colab import drive
drive.mount('/content/drive')
import geopandas as gpd

path = "/content/drive/MyDrive/Tri_Tue_Nhan_Tao/gadm41_VNM_1.json"

gdf = gpd.read_file(path)

gdf.head()

import geopandas as gpd
import matplotlib.pyplot as plt
import random
gdf["orders"] = [random.randint(100,1000) for i in range(len(gdf))]

gdf.plot(
    column="orders",
    cmap="OrRd",
    figsize=(12,14),
    legend=True,
    edgecolor="black"
)

plt.title("Số lượng đơn hàng theo tỉnh/thành Việt Nam")
plt.show()

#Bai 5

import folium


center_coords = [10.7629, 106.6822]


m = folium.Map(
    location=center_coords,
    zoom_start=12
)


folium.Marker(
    location=center_coords,
    popup="Trung tâm phân phối UEH",
    icon=folium.Icon(color="red")
).add_to(m)




folium.Circle(
    location=center_coords,
    radius=3000,
    color="green",
    fill=True,
    fill_opacity=0.2,
    popup="Vùng phục vụ 3 km"
).add_to(m)


folium.Circle(
    location=center_coords,
    radius=5000,
    color="blue",
    fill=True,
    fill_opacity=0.15,
    popup="Vùng phục vụ 5 km"
).add_to(m)


folium.Circle(
    location=center_coords,
    radius=10000,
    color="orange",
    fill=True,
    fill_opacity=0.1,
    popup="Vùng phục vụ 10 km"
).add_to(m)


folium.Marker([10.7750,106.6900], popup="Khách hàng A").add_to(m)
folium.Marker([10.7300,106.7000], popup="Khách hàng B").add_to(m)
folium.Marker([10.8200,106.7200], popup="Khách hàng C").add_to(m)


m

#Bài 6


import osmnx as ox
import matplotlib.pyplot as plt


place = "District 1, Ho Chi Minh City, Vietnam"


G = ox.graph_from_place(place, network_type="drive")


fig, ax = ox.plot_graph(
    G,
    node_size=12,          
    node_color="red",     
    edge_color="black",    
    edge_linewidth=0.6,
    bgcolor="white"
)


num_nodes = len(G.nodes)
num_edges = len(G.edges)

total_length = 0

for u, v, k, data in G.edges(keys=True, data=True):
    if "length" in data:
        total_length += data["length"]

avg_length = total_length / num_edges

print("Số nút giao:", num_nodes)
print("Số đoạn đường:", num_edges)
print("Tổng chiều dài đường (m):", round(total_length,2))
print("Chiều dài trung bình (m):", round(avg_length,2))

#Bài 7

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


place = "District 1, Ho Chi Minh City, Vietnam"


G = ox.graph_from_place(place, network_type="drive")


start_point = (10.7750, 106.7000)
end_point   = (10.7600, 106.6800)


orig = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
dest = ox.distance.nearest_nodes(G, end_point[1], end_point[0])


route1 = nx.shortest_path(
    G,
    orig,
    dest,
    weight="length",
    method="dijkstra"
)


route2 = nx.astar_path(
    G,
    orig,
    dest,
    weight="length"
)


fig, ax = ox.plot_graph_route(
    G,
    route1,
    route_color="red",
    route_linewidth=4,
    node_size=0,
    bgcolor="white"
)


len1 = nx.path_weight(G, route1, weight="length")
len2 = nx.path_weight(G, route2, weight="length")

print("Chiều dài tuyến Dijkstra (m):", round(len1,2))
print("Chiều dài tuyến A* (m):", round(len2,2))

#Bài 8


import folium
from geopy.distance import geodesic


center = [10.7629, 106.6822]

m = folium.Map(
    location=center,
    zoom_start=13
)


cars = {
    "Xe 1": [10.7700, 106.6900],
    "Xe 2": [10.7500, 106.6700],
    "Xe 3": [10.7800, 106.7000]
}


customers = {
    "Khách A": [10.7650, 106.6750],
    "Khách B": [10.7550, 106.6950],
    "Khách C": [10.7720, 106.6820]
}


for name, loc in cars.items():
    folium.Marker(
        location=loc,
        popup=name,
        icon=folium.Icon(color="blue")
    ).add_to(m)


for name, loc in customers.items():
    folium.Marker(
        location=loc,
        popup=name,
        icon=folium.Icon(color="red")
    ).add_to(m)


for cus_name, cus_loc in customers.items():

    min_distance = 999999
    best_car = ""
    best_loc = None

    for car_name, car_loc in cars.items():

        d = geodesic(car_loc, cus_loc).km

        if d < min_distance:
            min_distance = d
            best_car = car_name
            best_loc = car_loc

    folium.PolyLine(
        [best_loc, cus_loc],
        color="green",
        weight=3,
        popup=f"{best_car} -> {cus_name}"
    ).add_to(m)

m

#Bài 9

import folium
import random
import numpy as np
from sklearn.cluster import KMeans


center = [10.7629, 106.6822]

m = folium.Map(
    location=center,
    zoom_start=13
)


points = []

for i in range(60):
    lat = 10.7629 + random.uniform(-0.03, 0.03)
    lon = 106.6822 + random.uniform(-0.03, 0.03)
    points.append([lat, lon])

X = np.array(points)


kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

labels = kmeans.labels_
centers = kmeans.cluster_centers_


colors = ["red", "blue", "green"]


for i in range(len(points)):

    folium.CircleMarker(
        location=points[i],
        radius=5,
        color=colors[labels[i]],
        fill=True,
        fill_opacity=0.7
    ).add_to(m)


for c in centers:

    folium.Marker(
        location=[c[0], c[1]],
        popup="Kho hàng đề xuất",
        icon=folium.Icon(color="black")
    ).add_to(m)

m

#Bài 10

import folium

center = [10.7629, 106.6822]

m = folium.Map(
    location=center,
    zoom_start=13
)


start = [10.7500, 106.6650]
end   = [10.7800, 106.7050]

folium.Marker(
    location=start,
    popup="Điểm xuất phát",
    icon=folium.Icon(color="green")
).add_to(m)

folium.Marker(
    location=end,
    popup="Điểm đến",
    icon=folium.Icon(color="red")
).add_to(m)


jam1 = [
    start,
    [10.7580,106.6740],
    [10.7650,106.6830],
    [10.7720,106.6920]
]

jam2 = [
    [10.7600,106.6700],
    [10.7680,106.6780],
    [10.7750,106.6860],
    end
]

folium.PolyLine(
    jam1,
    color="red",
    weight=6,
    popup="Tuyến kẹt xe"
).add_to(m)

folium.PolyLine(
    jam2,
    color="red",
    weight=6,
    popup="Tuyến kẹt xe"
).add_to(m)


best_route = [
    start,
    [10.7540,106.6680],
    [10.7620,106.6760],
    [10.7700,106.6880],
    [10.7760,106.6970],
    end
]

folium.PolyLine(
    best_route,
    color="blue",
    weight=6,
    popup="Tuyến tối ưu"
).add_to(m)


alt_route = [
    start,
    [10.7520,106.6720],
    [10.7600,106.6820],
    [10.7680,106.6940],
    end
]

folium.PolyLine(
    alt_route,
    color="blue",
    weight=5,
    dash_array="10,10",
    popup="Tuyến thay thế"
).add_to(m)


m

#Bài 11

import pandas as pd
import numpy as np
import folium
from sklearn.ensemble import RandomForestRegressor


areas = ["Quan 1", "Quan 3", "Quan 5", "Binh Thanh", "Tan Binh"]

data = []

for area in areas:
    for hour in range(24):

        if area == "Quan 1":
            base = 140
        elif area == "Quan 3":
            base = 120
        elif area == "Quan 5":
            base = 95
        elif area == "Binh Thanh":
            base = 110
        else:
            base = 100

        if hour in [7,8,9]:
            demand = base + np.random.randint(50,90)

        elif hour in [17,18,19,20]:
            demand = base + np.random.randint(60,100)


        elif hour in [0,1,2,3,4]:
            demand = base - np.random.randint(30,50)

        else:
            demand = base + np.random.randint(0,35)

        data.append([area,hour,demand])

df = pd.DataFrame(data, columns=["area","hour","demand"])


mapping = {
    "Quan 1":1,
    "Quan 3":2,
    "Quan 5":3,
    "Binh Thanh":4,
    "Tan Binh":5
}

df["code"] = df["area"].map(mapping)


X = df[["code","hour"]]
y = df["demand"]

model = RandomForestRegressor(
    n_estimators=150,
    random_state=42
)

model.fit(X,y)


coords = {
    "Quan 1":[10.776,106.700],
    "Quan 3":[10.784,106.686],
    "Quan 5":[10.755,106.667],
    "Binh Thanh":[10.806,106.710],
    "Tan Binh":[10.801,106.653]
}


hour = int(input("Nhập giờ muốn xem (0-23): "))


m = folium.Map(
    location=[10.78,106.685],
    zoom_start=12
)

print("DỰ ĐOÁN NHU CẦU LÚC", hour, "GIỜ")
print("-"*40)

for area in areas:

    pred = int(model.predict([[mapping[area], hour]])[0])

    if pred >= 190:
        color = "red"
        radius = 18
        status = "RẤT CAO"

    elif pred >= 150:
        color = "orange"
        radius = 14
        status = "CAO"

    elif pred >= 110:
        color = "blue"
        radius = 12
        status = "TRUNG BÌNH"

    else:
        color = "green"
        radius = 10
        status = "THẤP"

    print(area, ":", pred, "-", status)

    folium.CircleMarker(
        location=coords[area],
        radius=radius,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=f"{area}<br>{hour}:00<br>{pred} cuốc<br>{status}"
    ).add_to(m)

m

#Bài 12

import folium
import random
import numpy as np
from sklearn.cluster import KMeans
from geopy.distance import geodesic

warehouse = [10.7629, 106.6822]

m = folium.Map(
    location=warehouse,
    zoom_start=13
)

folium.Marker(
    location=warehouse,
    popup="Kho trung tâm",
    icon=folium.Icon(color="red")
).add_to(m)

orders = []

for i in range(10):
    lat = 10.7629 + random.uniform(-0.03,0.03)
    lon = 106.6822 + random.uniform(-0.03,0.03)
    orders.append([lat,lon])

X = np.array(orders)


kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X)

labels = kmeans.labels_


colors = ["blue","green","orange"]


def nearest_route(points):

    remain = points.copy()
    route = []
    current = warehouse

    while len(remain) > 0:

        nearest = min(
            remain,
            key=lambda p: geodesic(current,p).km
        )

        route.append(nearest)
        remain.remove(nearest)
        current = nearest

    return route


for car in range(3):

    cluster_points = []

    for i in range(len(orders)):
        if labels[i] == car:
            cluster_points.append(orders[i])

    route_raw = [warehouse] + cluster_points + [warehouse]

    folium.PolyLine(
        route_raw,
        color=colors[car],
        weight=3,
        opacity=0.4,
        popup=f"Xe {car+1} - Chưa tối ưu"
    ).add_to(m)


    best = nearest_route(cluster_points)

    route_best = [warehouse] + best + [warehouse]

    folium.PolyLine(
        route_best,
        color=colors[car],
        weight=6,
        dash_array="10,10",
        popup=f"Xe {car+1} - Tối ưu"
    ).add_to(m)


for i in range(len(orders)):

    folium.CircleMarker(
        location=orders[i],
        radius=6,
        color=colors[labels[i]],
        fill=True,
        fill_opacity=0.8,
        popup=f"Đơn hàng {i+1}"
    ).add_to(m)

m

#Bài 13

import folium


center = [10.7629,106.6822]

m = folium.Map(
    location=center,
    zoom_start=13
)


point_layer = folium.FeatureGroup(name="Điểm dữ liệu")

folium.Marker(
    [10.7629,106.6822],
    popup="Kho trung tâm",
    icon=folium.Icon(color="red")
).add_to(point_layer)

folium.Marker(
    [10.7750,106.7000],
    popup="Chi nhánh Quận 1",
    icon=folium.Icon(color="blue")
).add_to(point_layer)

point_layer.add_to(m)


line_layer = folium.FeatureGroup(name="Tuyến giao hàng")

route = [
    [10.7629,106.6822],
    [10.7700,106.6900],
    [10.7750,106.7000]
]

folium.PolyLine(
    route,
    color="green",
    weight=5,
    popup="Tuyến giao hàng"
).add_to(line_layer)

line_layer.add_to(m)


area_layer = folium.FeatureGroup(name="Vùng phục vụ")

folium.Circle(
    location=center,
    radius=5000,
    color="orange",
    fill=True,
    fill_opacity=0.2,
    popup="Vùng phục vụ 5km"
).add_to(area_layer)

area_layer.add_to(m)


folium.LayerControl().add_to(m)

m

#Bài 14

import folium
import time
from IPython.display import display, clear_output


start = [10.7500, 106.6650]   
end   = [10.7800, 106.7050]   


speed = 2

total_frames = 30


frame = 0

while frame <= total_frames:

    ratio = frame / total_frames

    lat = start[0] + (end[0] - start[0]) * ratio
    lon = start[1] + (end[1] - start[1]) * ratio


    m = folium.Map(
        location=[10.765,106.685],
        zoom_start=13
    )


    folium.Marker(
        location=start,
        popup="Điểm đi",
        icon=folium.Icon(color="green")
    ).add_to(m)


    folium.Marker(
        location=end,
        popup="Điểm đến",
        icon=folium.Icon(color="red")
    ).add_to(m)


    folium.PolyLine(
        [start, end],
        color="blue",
        weight=4
    ).add_to(m)


    folium.CircleMarker(
        location=[lat, lon],
        radius=8,
        color="black",
        fill=True,
        fill_opacity=1,
        popup=f"Frame {frame}"
    ).add_to(m)

    clear_output(wait=True)
    display(m)

    time.sleep(1)

    frame += speed

#Bài 15

import osmnx as ox
import networkx as nx
import folium
import time
from IPython.display import display, clear_output


place = "District 1, Ho Chi Minh City, Vietnam"

G = ox.graph_from_place(place, network_type="drive")


driver = (10.7750, 106.7000)
customer = (10.7650, 106.6850)
destination = (10.7780, 106.6950)


driver_node = ox.distance.nearest_nodes(G, driver[1], driver[0])
customer_node = ox.distance.nearest_nodes(G, customer[1], customer[0])
dest_node = ox.distance.nearest_nodes(G, destination[1], destination[0])


route_pickup = nx.shortest_path(
    G,
    driver_node,
    customer_node,
    weight="length"
)

route_trip = nx.shortest_path(
    G,
    customer_node,
    dest_node,
    weight="length"
)


def node_to_coord(node):
    return [G.nodes[node]["y"], G.nodes[node]["x"]]


for i in range(len(route_pickup)):

    pos = node_to_coord(route_pickup[i])

    m = folium.Map(
        location=[10.772,106.692],
        zoom_start=14
    )


    pickup_coords = [node_to_coord(n) for n in route_pickup]

    folium.PolyLine(
        pickup_coords,
        color="blue",
        weight=5
    ).add_to(m)


    folium.Marker(
        location=customer,
        popup="Khách hàng",
        icon=folium.Icon(color="red")
    ).add_to(m)


    folium.Marker(
        location=destination,
        popup="Điểm đến",
        icon=folium.Icon(color="green")
    ).add_to(m)


    folium.Marker(
        location=pos,
        popup="Tài xế đang đón khách",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    clear_output(wait=True)
    display(m)
    time.sleep(0.15)


for i in range(len(route_trip)):

    pos = node_to_coord(route_trip[i])

    m = folium.Map(
        location=[10.772,106.692],
        zoom_start=14
    )

    trip_coords = [node_to_coord(n) for n in route_trip]

    folium.PolyLine(
        trip_coords,
        color="purple",
        weight=5
    ).add_to(m)


    folium.Marker(
        location=pos,
        popup="Đang chở khách",
        icon=folium.Icon(color="purple")
    ).add_to(m)


    folium.Marker(
        location=destination,
        popup="Điểm đến",
        icon=folium.Icon(color="green")
    ).add_to(m)

    clear_output(wait=True)
    display(m)
    time.sleep(0.15)