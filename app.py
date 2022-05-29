from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
all_rest = pd.read_csv("restaurants.csv")

def fav(rest_df1):
    rest_df1 = rest_df1.reset_index()
    from sklearn.feature_extraction.text import CountVectorizer

    count1 = CountVectorizer(stop_words='english')
    count2 = count1.fit_transform(rest_df1['highlights'])
    from sklearn.metrics.pairwise import cosine_similarity

    cosine_sim2 = cosine_similarity(count2, count2)

    sim = list(enumerate(cosine_sim2[0]))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:11]
    ind = [i[0] for i in sim]

    final = rest_df1.copy().iloc[ind[0]]
    final = pd.DataFrame(final)
    final = final.T

    for i in range(1, len(ind)):
        final1 = rest_df1.copy().iloc[ind[i]]
        final1 = pd.DataFrame(final1)
        final1 = final1.T
        final = pd.concat([final, final1])

    return final


def rest_rec(cost, people=2, min_cost=0, cuisine=[], Locality=[], fav_rest="", all_rest=all_rest):
    cost = cost + 200

    x = cost / people
    y = min_cost / people

    rest_df1 = all_rest.copy().loc[all_rest['locality'] == Locality[0]]

    for i in range(1, len(Locality)):
        rest_df2 = all_rest.copy().loc[all_rest['locality'] == Locality[i]]
        rest_df1 = pd.concat([rest_df1, rest_df2])
        rest_df1.drop_duplicates(subset='name', keep='last', inplace=True)

    rest_dflocal = rest_df1.copy()

    rest_dflocal = rest_dflocal.loc[rest_dflocal['average_cost_for_one'] <= x]
    rest_dflocal = rest_dflocal.loc[rest_dflocal['average_cost_for_one'] >= y]

    rest_dflocal['Start'] = rest_dflocal['cuisines'].str.find(cuisine[0])
    rest_dfcui = rest_dflocal.copy().loc[rest_dflocal['Start'] >= 0]

    for i in range(1, len(cuisine)):
        rest_dflocal['Start'] = rest_dflocal['cuisines'].str.find(cuisine[i])
        lko_rest_cu = rest_dflocal.copy().loc[rest_dflocal['Start'] >= 0]
        rest_dfcui = pd.concat([rest_dfcui, lko_rest_cu])
        rest_dfcui.drop_duplicates(subset='name', keep='last', inplace=True)

    if fav_rest != "":

        favr = all_rest.loc[all_rest['name'] == fav_rest].drop_duplicates()
        favr = pd.DataFrame(favr)
        lko_rest3 = pd.concat([favr, rest_dfcui])
        lko_rest3.drop('Start', axis=1, inplace=True)
        rest_selected = fav(lko_rest3)
    else:
        rest_dfcui = rest_dfcui.sort_values('scope', ascending=False)
        rest_selected = rest_dfcui.head(10)
    return rest_selected


def calc(max_Price, people, min_Price, cuisine, locality):
    rest_sugg = rest_rec(max_Price, people, min_Price, [cuisine], [locality])
    rest_df1 = rest_sugg.copy().loc[:,
                 ['name', 'address', 'locality', 'timings', 'aggregate_rating', 'url', 'cuisines']]
    rest_df_final = pd.DataFrame(rest_df1)
    rest_df_final = rest_df_final.reset_index()
    rest_df_final = rest_df_final.rename(columns={'index': 'res_id'})
    rest_df_final.drop('res_id', axis=1, inplace=True)
    rest_df_final = rest_df_final.T
    rest_df_final = rest_df_final
    ans = rest_df_final.to_dict()
    res = [value for value in ans.values()]
    return res


@app.route("/")
@app.route("/home", methods=['POST','GET'])
def home():
    return render_template('home.html')


@app.route("/search", methods=['POST','GET'])
def search():
    if request.method == 'POST':
        people = int(request.form['people'])
        min_Price = int(request.form['min_Price'])
        max_Price =int(request.form['max_Price'])
        cuisine1 = request.form['cuisine']
        locality1 = request.form['locality']
        res = calc(max_Price, people, min_Price,cuisine1, locality1)
        return render_template('search.html', title='Search', restaurants=res)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
