from pyvis.network import Network
import pandas as pd

df = pd.read_excel('data.xlsx')

#create the network
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True , filter_menu=True, select_menu=True)
net.repulsion(central_gravity=0)



#create nodes
for index, row in df.iterrows():
    faculty_information = f"{df.iloc[index]['Name of Faculty']}\n{df.iloc[index]['Course']}"
    net.add_node(row['Name of Faculty'], label=row['Name of Faculty'], title=faculty_information, color="red")
    net.add_node(row['Author'], label=row['Author'], title=row['Author'], color = "green")
    net.add_node(row['Title'], label=row['Title'], title=row['Title'])
    net.add_edge(row['Author'], row['Title'], color = "green", width=3)

#connecting edges
for i in range(len(df)):
    for j in range(i+1, len(df)):
        if df.iloc[i]["Name of Faculty"]==df.iloc[j]["Name of Faculty"]:
            net.add_edge(df.iloc[i]['Name of Faculty'], df.iloc[j]['Title'], color="red")
            net.add_edge(df.iloc[i]['Name of Faculty'], df.iloc[i]['Title'], color="red")




net.show_buttons(filter_=['physics'])


# Show the graph
net.show("index.html")