{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8852d435",
   "metadata": {
    "dc": {
     "key": "4"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 1. Loading your friend's data into a dictionary\n",
    "<p><img src=\"https://assets.datacamp.com/production/project_1237/img/netflix.jpg\" alt=\"Someone's feet on table facing a television\"></p>\n",
    "<p>Netflix! What started in 1997 as a DVD rental service has since exploded into the largest entertainment/media company by <a href=\"https://www.marketwatch.com/story/netflix-shares-close-up-8-for-yet-another-record-high-2020-07-10\">market capitalization</a>, boasting over 200 million subscribers as of <a href=\"https://www.cbsnews.com/news/netflix-tops-200-million-subscribers-but-faces-growing-challenge-from-disney-plus/\">January 2021</a>.</p>\n",
    "<p>Given the large number of movies and series available on the platform, it is a perfect opportunity to flex our data manipulation skills and dive into the entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV file containing Netflix data. For their first order of business, they have been performing some analyses, and they believe that the average duration of movies has been declining. </p>\n",
    "<p>As evidence of this, they have provided us with the following information. For the years from 2011 to 2020, the average movie durations are 103, 101, 99, 100, 100, 95, 95, 96, 93, and 90, respectively.</p>\n",
    "<p>If we're going to be working with this data, we know a good place to start would be to probably start working with <code>pandas</code>. But first we'll need to create a DataFrame from scratch. Let's start by creating a Python object covered in <a href=\"https://learn.datacamp.com/courses/intermediate-python\">Intermediate Python</a>: a dictionary!</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "53d415d4",
   "metadata": {
    "dc": {
     "key": "4"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'years': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], 'durations': [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]}\n"
     ]
    }
   ],
   "source": [
    "# Create the years and durations lists\n",
    "years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]\n",
    "durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]\n",
    "\n",
    "# Create a dictionary with the two lists\n",
    "movie_dict = {\"years\": years, \"durations\": durations}\n",
    "\n",
    "# Print the dictionary\n",
    "print(movie_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54f59595",
   "metadata": {
    "dc": {
     "key": "11"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 2. Creating a DataFrame from a dictionary\n",
    "<p>To convert our dictionary <code>movie_dict</code> to a <code>pandas</code> DataFrame, we will first need to import the library under its usual alias. We'll also want to inspect our DataFrame to ensure it was created correctly. Let's perform these steps now.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "02f383ff",
   "metadata": {
    "dc": {
     "key": "11"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>years</th>\n",
       "      <th>durations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2011</td>\n",
       "      <td>103</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2012</td>\n",
       "      <td>101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2013</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2014</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2015</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2016</td>\n",
       "      <td>95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2017</td>\n",
       "      <td>95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2018</td>\n",
       "      <td>96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2019</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2020</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   years  durations\n",
       "0   2011        103\n",
       "1   2012        101\n",
       "2   2013         99\n",
       "3   2014        100\n",
       "4   2015        100\n",
       "5   2016         95\n",
       "6   2017         95\n",
       "7   2018         96\n",
       "8   2019         93\n",
       "9   2020         90"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import pandas under its usual alias\n",
    "import pandas as pd\n",
    "\n",
    "# Create a DataFrame from the dictionary\n",
    "durations_df = pd.DataFrame(movie_dict)\n",
    "\n",
    "# Print the DataFrame\n",
    "durations_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "034a14be",
   "metadata": {
    "dc": {
     "key": "18"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 3. A visual inspection of our data\n",
    "<p>Alright, we now have a <code>pandas</code> DataFrame, the most common way to work with tabular data in Python. Now back to the task at hand. We want to follow up on our friend's assertion that movie lengths have been decreasing over time. A great place to start will be a visualization of the data.</p>\n",
    "<p>Given that the data is continuous, a line plot would be a good choice, with the dates represented along the x-axis and the average length in minutes along the y-axis. This will allow us to easily spot any trends in movie durations. There are many ways to visualize data in Python, but <code>matploblib.pyplot</code> is one of the most common packages to do so.</p>\n",
    "<p><em>Note: In order for us to correctly test your plot, you will need to initalize a <code>matplotlib.pyplot</code> Figure object, which we have already provided in the cell below. You can continue to create your plot as you have learned in Intermediate Python.</em></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "fb428df4",
   "metadata": {
    "dc": {
     "key": "18"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import matplotlib.pyplot under its usual alias and create a figure\n",
    "import matplotlib.pyplot as plt\n",
    "fig = plt.figure()\n",
    "\n",
    "# Draw a line plot of release_years and durations\n",
    "plt.plot(durations_df['years'], durations_df['durations'])\n",
    "# Create a title\n",
    "plt.title(\"Netflix Movie Durations 2011-2020\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6276493b",
   "metadata": {
    "dc": {
     "key": "25"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 4. Loading the rest of the data from a CSV\n",
    "<p>Well, it looks like there is something to the idea that movie lengths have decreased over the past ten years! But equipped only with our friend's aggregations, we're limited in the further explorations we can perform. There are a few questions about this trend that we are currently unable to answer, including:</p>\n",
    "<ol>\n",
    "<li>What does this trend look like over a longer period of time?</li>\n",
    "<li>Is this explainable by something like the genre of entertainment?</li>\n",
    "</ol>\n",
    "<p>Upon asking our friend for the original CSV they used to perform their analyses, they gladly oblige and send it. We now have access to the CSV file, available at the path <code>\"datasets/netflix_data.csv\"</code>. Let's create another DataFrame, this time with all of the data. Given the length of our friend's data, printing the whole DataFrame is probably not a good idea, so we will inspect it by printing only the first five rows.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "95d63a9f",
   "metadata": {
    "dc": {
     "key": "25"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>show_id</th>\n",
       "      <th>type</th>\n",
       "      <th>title</th>\n",
       "      <th>director</th>\n",
       "      <th>cast</th>\n",
       "      <th>country</th>\n",
       "      <th>date_added</th>\n",
       "      <th>release_year</th>\n",
       "      <th>duration</th>\n",
       "      <th>description</th>\n",
       "      <th>genre</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s1</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>3%</td>\n",
       "      <td>NaN</td>\n",
       "      <td>João Miguel, Bianca Comparato, Michel Gomes, R...</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>August 14, 2020</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "      <td>In a future where the elite inhabit an island ...</td>\n",
       "      <td>International TV</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s2</td>\n",
       "      <td>Movie</td>\n",
       "      <td>7:19</td>\n",
       "      <td>Jorge Michel Grau</td>\n",
       "      <td>Demián Bichir, Héctor Bonilla, Oscar Serrano, ...</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>December 23, 2016</td>\n",
       "      <td>2016</td>\n",
       "      <td>93</td>\n",
       "      <td>After a devastating earthquake hits Mexico Cit...</td>\n",
       "      <td>Dramas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>s3</td>\n",
       "      <td>Movie</td>\n",
       "      <td>23:59</td>\n",
       "      <td>Gilbert Chan</td>\n",
       "      <td>Tedd Chan, Stella Chung, Henley Hii, Lawrence ...</td>\n",
       "      <td>Singapore</td>\n",
       "      <td>December 20, 2018</td>\n",
       "      <td>2011</td>\n",
       "      <td>78</td>\n",
       "      <td>When an army recruit is found dead, his fellow...</td>\n",
       "      <td>Horror Movies</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>s4</td>\n",
       "      <td>Movie</td>\n",
       "      <td>9</td>\n",
       "      <td>Shane Acker</td>\n",
       "      <td>Elijah Wood, John C. Reilly, Jennifer Connelly...</td>\n",
       "      <td>United States</td>\n",
       "      <td>November 16, 2017</td>\n",
       "      <td>2009</td>\n",
       "      <td>80</td>\n",
       "      <td>In a postapocalyptic world, rag-doll robots hi...</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>s5</td>\n",
       "      <td>Movie</td>\n",
       "      <td>21</td>\n",
       "      <td>Robert Luketic</td>\n",
       "      <td>Jim Sturgess, Kevin Spacey, Kate Bosworth, Aar...</td>\n",
       "      <td>United States</td>\n",
       "      <td>January 1, 2020</td>\n",
       "      <td>2008</td>\n",
       "      <td>123</td>\n",
       "      <td>A brilliant group of students become card-coun...</td>\n",
       "      <td>Dramas</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  show_id     type  title           director  \\\n",
       "0      s1  TV Show     3%                NaN   \n",
       "1      s2    Movie   7:19  Jorge Michel Grau   \n",
       "2      s3    Movie  23:59       Gilbert Chan   \n",
       "3      s4    Movie      9        Shane Acker   \n",
       "4      s5    Movie     21     Robert Luketic   \n",
       "\n",
       "                                                cast        country  \\\n",
       "0  João Miguel, Bianca Comparato, Michel Gomes, R...         Brazil   \n",
       "1  Demián Bichir, Héctor Bonilla, Oscar Serrano, ...         Mexico   \n",
       "2  Tedd Chan, Stella Chung, Henley Hii, Lawrence ...      Singapore   \n",
       "3  Elijah Wood, John C. Reilly, Jennifer Connelly...  United States   \n",
       "4  Jim Sturgess, Kevin Spacey, Kate Bosworth, Aar...  United States   \n",
       "\n",
       "          date_added  release_year  duration  \\\n",
       "0    August 14, 2020          2020         4   \n",
       "1  December 23, 2016          2016        93   \n",
       "2  December 20, 2018          2011        78   \n",
       "3  November 16, 2017          2009        80   \n",
       "4    January 1, 2020          2008       123   \n",
       "\n",
       "                                         description             genre  \n",
       "0  In a future where the elite inhabit an island ...  International TV  \n",
       "1  After a devastating earthquake hits Mexico Cit...            Dramas  \n",
       "2  When an army recruit is found dead, his fellow...     Horror Movies  \n",
       "3  In a postapocalyptic world, rag-doll robots hi...            Action  \n",
       "4  A brilliant group of students become card-coun...            Dramas  "
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read in the CSV as a DataFrame\n",
    "netflix_df = pd.read_csv(\"datasets/netflix_data.csv\")\n",
    "\n",
    "# Print the first five rows of the DataFrame\n",
    "netflix_df[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f7084b5",
   "metadata": {
    "dc": {
     "key": "32"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 5. Filtering for movies!\n",
    "<p>Okay, we have our data! Now we can dive in and start looking at movie lengths. </p>\n",
    "<p>Or can we? Looking at the first five rows of our new DataFrame, we notice a column <code>type</code>. Scanning the column, it's clear there are also TV shows in the dataset! Moreover, the <code>duration</code> column we planned to use seems to represent different values depending on whether the row is a movie or a show (perhaps the number of minutes versus the number of seasons)?</p>\n",
    "<p>Fortunately, a DataFrame allows us to filter data quickly, and we can select rows where <code>type</code> is <code>Movie</code>. While we're at it, we don't need information from all of the columns, so let's create a new DataFrame <code>netflix_movies</code> containing only <code>title</code>, <code>country</code>, <code>genre</code>, <code>release_year</code>, and <code>duration</code>.</p>\n",
    "<p>Let's put our data subsetting skills to work!</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "ae60c32a",
   "metadata": {
    "dc": {
     "key": "32"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>country</th>\n",
       "      <th>genre</th>\n",
       "      <th>release_year</th>\n",
       "      <th>duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7:19</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>Dramas</td>\n",
       "      <td>2016</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>23:59</td>\n",
       "      <td>Singapore</td>\n",
       "      <td>Horror Movies</td>\n",
       "      <td>2011</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>9</td>\n",
       "      <td>United States</td>\n",
       "      <td>Action</td>\n",
       "      <td>2009</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>21</td>\n",
       "      <td>United States</td>\n",
       "      <td>Dramas</td>\n",
       "      <td>2008</td>\n",
       "      <td>123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>122</td>\n",
       "      <td>Egypt</td>\n",
       "      <td>Horror Movies</td>\n",
       "      <td>2019</td>\n",
       "      <td>95</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   title        country          genre  release_year  duration\n",
       "1   7:19         Mexico         Dramas          2016        93\n",
       "2  23:59      Singapore  Horror Movies          2011        78\n",
       "3      9  United States         Action          2009        80\n",
       "4     21  United States         Dramas          2008       123\n",
       "6    122          Egypt  Horror Movies          2019        95"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Subset the DataFrame for type \"Movie\"\n",
    "netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']\n",
    "\n",
    "# Select only the columns of interest\n",
    "netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]\n",
    "# Print the first five rows of the new DataFrame\n",
    "netflix_movies_col_subset[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b68b481e",
   "metadata": {
    "dc": {
     "key": "39"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 6. Creating a scatter plot\n",
    "<p>Okay, now we're getting somewhere. We've read in the raw data, selected rows of movies, and have limited our DataFrame to our columns of interest. Let's try visualizing the data again to inspect the data over a longer range of time.</p>\n",
    "<p>This time, we are no longer working with aggregates but instead with individual movies. A line plot is no longer a good choice for our data, so let's try a scatter plot instead. We will again plot the year of release on the x-axis and the movie duration on the y-axis.</p>\n",
    "<p><em>Note: Although not taught in Intermediate Python, we have provided you the code <code>fig = plt.figure(figsize=(12,8))</code> to increase the size of the plot (to help you see the results), as well as to assist with testing. For more information on how to create or work with a <code>matplotlib</code> <code>figure</code>, refer to the <a href=\"https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html\">documentation</a>.</em></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "43ec236a",
   "metadata": {
    "dc": {
     "key": "39"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "image/png": "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r7zyCi655BLccMMNkfOks7MTV155Jf70pz/hgQceiEloovVmP08++STGjx9v209nZyd++MMf4oknnsCll14auf/r9ddfx9atW7F48WLccMMNtt/p6OiIzE4CvTsfiMgbOANFRL1y3nnnobOzM1KGtWPHDrz66qtYuHAhcnJylL+zYcMG/Pvf/8a0adNiLppPOOEEfPOb38SePXvw0ksvReLh7aJnKv7973/jvffewzHHHIMDDjigx2N94oknUFNTg6uvvtqWPAHA5MmT8f/+3//Drl27jF/IjB49GgBQXV1tZH/nnXdeTPIEAOnp6THJEwDk5eXh3HPPRW1tLd57770+PXZbWxueeOIJZGVl4frrr7clHfvttx/+53/+B6FQKGZWEgCysrLw61//OnIxCwBTpkzBzJkzsXnzZjQ0NCR0LFdddZWtlCwzMxPLli0DAFtZ4Ne+9jVMmzYNr7zyCnbt2hWJh0Ih/OlPf0J6ejrOPfdc8eMGAgHce++9yMnJwZ/+9KdIaV/4eT3wwANoaWnBb37zG9vFMgAcd9xxmDdvHj788EP8+9//jsTHjBmjTNpPPPFETJkyxTYja1VYWBhJ3CT68vr11tq1a7FixQqsWLEC11xzDY4//ng88sgjGDNmDH79619Htuvs7MTdd9+NgoICrFixwnaepKSk4LrrroPP58Nf/vKXHh+vt/uJTp7C2y9evBgAlK+BqsGK3++3nZe9OR+IyBs4A0VEvXLEEUfgsMMOw6OPPoqf/exn+POf/4yOjo4ey/c+/PBDANDOxpxwwgl44YUX8OGHH0ZmEebPn4+8vDysWrUKy5cvR2pqKgBEyvoksxcbNmwAAHzyySfKNWz+85//AOiajTrllFPi7k8qXK4kneGIZ/r06dqfffbZZ/jd736Ht956C7t370Zzc7Pt5+FmAL31+eefY9++fTjyyCOVTTpOOOEEAN2vsdWECRMwZMiQmHi4U2Jtba026VaZNWtWTOyYY46Bz+eLKYm66KKL8KMf/Qh//vOfI6V3r732GrZu3Yr/+q//wrBhw8SPC3RdbF900UW44447cOGFF9qS9/B59tZbbynHoaqqCkDXeRZO5EOhEJ588kk89thj+Pjjj1FbW2u77yYtLU15HIceemhCs6V9ef16q6SkBCUlJbZYUVERXn75ZVvC/5///AfV1dUYP348br75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HsfcWRxv53HMnZWM453UCRQREREREZFJTKCIiIiIiIiEmEAREREREREJMYEiIiIiIiISYgJFREREREQkxASKiIiIiIhIiAkUERERERGREBMoIiIiIiIiISZQREREREREQkygiIiIiIiIhJhAERERERERCTGBIiIiIiIiEmICRUREREREJMQEioiIiIiISIgJFBERERERkRATKCIiIiIiIiEmUEREREREREKBgT4AIiIiIiJyh7JgG5a/F0TFvg6MzvJj2bRcjMtNHejDchUmUEREREREhLJgG85YXY2twY5IbGNVK56dO5xJlAVL+IiIiIiICMvfC9qSJwDYGuzA8veCA3RE7sQEioiIiIiIULGvQxnfpYkPVkygiIiIiIgIo7P8yvgoTXywYgJFRERERERYNi0X43PtydL43K5GEtSNTSSIiIiIiAjjclPx7NzhWP5eELv2dWAUu/ApMYEiIiIiIiIAXUnUfccPG+jDcDWW8BEREREREQkxgSIiIiIiIhJiAkVERERERCTEBIqIiIiIiEiICRQREREREZEQEygiIiIiIiIhJlBERERERERCTKCIiIiIiIiEmEAREREREREJxU2g7rvvPhxzzDHYf//9sf/+++Mb3/gGVq9eHfl5KBTCihUrMGXKFIwaNQrz58/HZ599ZttHbW0tFi1ahKKiIhQVFWHRokWora01/mSIiIiIiIj6U9wEasyYMbjuuuvw+uuvY82aNZg9ezbOPfdcfPzxxwCAO+64A3fddRduvPFG/Otf/0JBQQG+/e1vIxgMRvZx8cUXY9OmTVi1ahVWrVqFTZs24dJLL+2/Z0VERERERNQP4iZQ8+fPxze+8Q1MmDABBx54IH75y18iJycH77zzDkKhEFauXIkf//jHWLBgAQ4++GCsXLkSDQ0NWLVqFQBg8+bNePXVV3H77bdjxowZmDFjBm677TasXr0apaWl/f4EiYiIiIiITEnoHqiOjg48/fTTaGxsxIwZM1BWVobdu3fjxBNPjGyTmZmJY445Bhs2bAAAvP3228jJycHMmTMj2xx99NHIzs6ObENEREREROQFAclGn3zyCU455RQ0NzcjOzsbjzzyCA455JBIAlRQUGDbvqCgABUVFQCAyspKDB8+HD6fL/Jzn8+HESNGoLKyssfHNTFDxVku53HMncXxdh7H3Fkcb+dxzJ3F8XYex9xZXhvv4uLiHn8uSqCKi4vx5ptvor6+Hs899xyWLFmCv/3tb0YOMN7j9kVpaWmf90GJ4Zg7i+PtPI65szjezuOYO4vj7TyOubOScbxFJXxpaWmYMGECjjjiCFx77bWYOnUq/vCHP2DkyJEAgKqqKtv2VVVVKCwsBAAUFhaiuroaoVAo8vNQKIQ9e/ZEtiEiIiIiIvKCXq0D1dnZidbWVowbNw4jR47EmjVrIj9rbm7GunXrIvc8zZgxAw0NDXj77bcj27z99ttobGy03RdFRERERETkdnFL+H71q1/hlFNOwX777Rfprrd27Vo8+eST8Pl8WLJkCW699VYUFxfjwAMPxC233ILs7GyceeaZAIDJkyfj5JNPxpVXXonbb78dAHDllVdi7ty5STedR0REREREyS1uArV7924sWrQIlZWVGDJkCA455BCsWrUKJ510EgDgiiuuQFNTE6666irU1tZi+vTpeOaZZ5CbmxvZx/3334+f/exnWLhwIQBg3rx5uOmmm/rpKREREREREfWPuAnUypUre/y5z+fD0qVLsXTpUu02+fn5uPfeexM/OiIiIiIiIhfp1T1QREREREREgxETKCIiIiIiIiEmUEREREREREJMoIiIiIiIiISYQBEREREREQkxgSIiIiIiIhJiAkVERERERCTEBIqIiIiIiEiICRQREREREZEQEygiIiIiIiIhJlBERERERERCTKCIiIiIiIiEmEAREREREREJMYEiIiIiIiISYgJFREREREQkxASKiIiIiIhIiAkUERERERGREBMoIiIiIiIiISZQREREREREQkygiIiIiIiIhJhAERERERERCTGBIiIiIiIiEmICRUREREREJMQEioiIiIiISIgJFBERERERkRATKCIiIiIiIiEmUEREREREREJMoIiIiIiIiISYQBEREREREQkxgSIiIiIiIhJiAkVERERERCTEBIqIiIiIiEiICRQREREREZEQEygiIiIiIiIhJlBERERERERCTKCIiIiIiIiEmEAREREREREJMYEiIiIiIiISYgJFREREREQkxASKiIiIiIhIiAkUERERERGREBMoIiIiIiIiISZQREREREREQkygiIiIiIiIhJhAERERERERCTGBIiIiIiIiEmICRUREREREJMQEioiIiIiISIgJFBERERERkRATKCIiIiIiIiEmUEREREREREJMoIiIiIiIiISYQBEREREREQkxgSIiIiIiIhJiAkVERERERCTEBIqIiIiIiEiICRQREREREZEQEygiIiIiIiIhJlBERERERERCTKCIiIiIiIiEAgN9AEREZFcWbMPy94Ko2NeB0Vl+LJuWi3G5qQN9WERERAQmUERErlIWbMMZq6uxNdgRiW2sasWzc4cziSIiInIBlvAREbnI8veCtuQJALYGO7D8veAAHRERERFZxU2gbr31VsyZMwf7778/Jk6ciLPPPhuffvqpbZslS5YgPz/f9r+TTz7Ztk1LSwuuuuoqTJgwAWPGjME555yDHTt2mH02REQeV7GvQxnfpYkTERGRs+ImUGvXrsVFF12E1atX4/nnn0cgEMAZZ5yBvXv32rY74YQTsHnz5sj/nnrqKdvPly5dihdeeAEPPPAAXnrpJQSDQZx99tno6OBFARFR2OgsvzI+ShMnIiIiZ8W9B+qZZ56x/fuee+5BUVER1q9fj3nz5kXi6enpGDlypHIfdXV1+POf/4y77roLc+bMiexn6tSpeO2113DSSSf15TkQESWNZdNysbGq1VbGNz63q5EEERERDbyE74FqaGhAZ2cn8vPzbfF169bhwAMPxPTp0/Hf//3fqKqqivzsgw8+QFtbG0488cRIbOzYsZg8eTI2bNjQ+6MnIkoy43JT8ezc4ThrQiaOG5WGsyZksoEEERGRiyTche+aa67B1KlTMWPGjEjs5JNPxre+9S2MGzcO27dvx/Lly3H66afjtddeQ3p6OiorK+H3+zF8+HDbvgoKClBZWdn3Z0FElETG5abivuOHDfRhEBERkUJCCdTPf/5zrF+/Hq+88gr8/u56/IULF0b++5BDDsERRxyBqVOnYvXq1Tj99NN7fXClpaW9/l2T+6DEcMydxfF2HsfcWRxv53HMncXxdh7H3FleG+/i4uIefy5OoJYuXYpnnnkGL7zwAg444IAetx09ejTGjBmDLVu2AAAKCwvR0dGB6upqjBgxIrJdVVUVvv71r/f64OMpLS3t8z4oMRxzZ3G8nccxdxbH23kcc2dxvJ3HMXdWMo636B6oq6++Gk8//TSef/55TJo0Ke721dXVqKioiDSVOOKII5Camoo1a9ZEttmxYwc2b96MmTNn9vLQiYiIiIiInBV3BuqnP/0p/vKXv+CRRx5Bfn4+du/eDQDIzs5GTk4OGhoacMMNN+D000/HyJEjsX37dlx//fUoKCjAN7/5TQBAXl4efvCDH+Daa69FQUEBhg4dil/84hc45JBDcMIJJ/TrEyQiIiIiIjIlbgJ1//33AwAWLFhgi1999dVYunQp/H4/Pv30UzzxxBOoq6vDyJEjcdxxx+GPf/wjcnO72+6uWLECfr8fF1xwAZqbmzF79mzcfffdtnupiIiIiIiI3CxuAlVbW9vjzzMzM2PWilJJT0/HzTffjJtvvll8cERERERERG6S8DpQREREREREgxUTKCIiIiIiIiEmUEREREREREJMoIiIiIiIiISYQBEREREREQkxgSIiIiIiIhJiAkVERERERCTEBIqIiIiIiEiICRQREREREZEQEygiIiIiIiKhwEAfABERDS5lwTYsfy+Iin0dGJ3lx7JpuRiXmzrQh0VERCTCBIqIiBxTFmzDGaursTXYEYltrGrFs3OHM4kiIiJPYAkfERE5Zvl7QVvyBABbgx1Y/l5wgI6IiIgoMUygiIjIMRX7OpTxXZo4ERGR2zCBIiIix4zO8ivjozRxIiIit2ECRUREjlk2LRfjc+3J0vjcrkYSREREXsAmEkRE5Jhxual4du5wLH8viF37OjDKgS587PpHREQmMYEiIiJHjctNxX3HD3Pksdj1j4iITGMJHxERJS12/SMiItOYQBERUdJi1z8iIjKNJXxERJS0THb9471UREQEMIEiIqIktmxaLjZWtdrK+HrT9Y/3UhERURhL+IiIKGmFu/6dNSETx41Kw1kTMnuV9PBeKiIiCuMMFBEZwfImcisTXf94LxUREYUxgSKiPmN5EyU7k/dSERGRt7GEj4j6jOVNlOyWTcvF+Fx7stSbe6mIiMj7OANFRH3G8iZKduF7qZa/F8SufR0YxTJVIqJBiwkUEfUZy5toMDBxLxUREXkfS/iIqM9Y3kRERESDBWegiKjPWN5ERGQeu5sSuRMTKCIyguVNRETmsLspkXuxhI+IiIjIZdjdlMi9mEARERERuQy7mxK5FxMoIiIiIpdhd1Mi92ICRUREROQy7G5K5F5sIkFERETkMuxuSuReTKCIiIiIXIjdTYnciSV8REREREREQkygiIiIiIiIhJhAERERERERCTGBIiIiIiIiEmICRUREREREJMQEioiIiIiISIgJFBERERERkRDXgSIiIiIi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qKmpwc0334zdu3fjoIMOwpNPPomioiInD4OIiIiIiKhXHG8icfHFF+Piiy92+mGJiIiIiIj6zNGFdImIiIiIiLyMCRQREREREZEQEygiIiIiIiIhJlBERERERERCTKCIiIiIiIiEmEAREREREREJMYEiIiIiIiISYgJFREREREQkxASKiIiIiIhIiAkUERERERGREBMoIiIiIiIiIV9tbW1ooA+CiIiIiIjICzgDRUREREREJMQEioiIiIiISIgJFBERERERkRATKCIiIiIiIiEmUEREREREREKuTqBKSkpwzjnn4KCDDkJ+fj4effRR288rKyuxZMkSTJkyBaNHj8bChQvxxRdfKPcVCoVw5plnIj8/H88995ztZ7W1tVi0aBGKiopQVFSERYsWoba2tr+elquZGPP58+cjPz/f9r8LL7zQtg3HvIupc/zdd9/FGWecgf322w9jx47FKaecgurq6sjPOd7d+jrmZWVlMed3+H+/+93vItu1tLTgqquuwoQJEzBmzBicc8452LFjh2PP0y1MnOO7d+/GokWLMGnSJIwePRqzZs3Ck08+aduG53g3E2O+detWnHvuuZg4cSL2339/nH/++aisrLRtwzHvcuutt2LOnDnYf//9MXHiRJx99tn49NNPbduEQiGsWLECU6ZMwahRozB//nx89tlntm0k4/nJJ5/gtNNOw6hRo3DQQQfhxhtvRCg0uJopmxrvW265BXPnzsWYMWOQn5+vfKwvv/wSZ5/9/9u796Coyj6A49919VVHJlGWRQVRGVi8IdgFsbIM0iJJJW8YWTKaipdmLEJMJAtLxEs06GQGaQakDYZCqY2TiOhga2OGWeINNRwDQiLYFG3h/YPx6AbkUVZc5PeZ4Q8Ph8M+33nc4Tm75+wkevTogZubG5GRkVy9evVuDc1mWaP5uXPnmDt3Lt7e3nTr1g1vb2/eeecdLl++bHGcltLcphdQJpOJ/v37ExcXR8eOHS2+V1tbS2hoKGfOnCE1NZV9+/bRs2dPxowZg8lkqnesNWvW0KZNw8OdPn06+fn5pKenk56eTn5+PjNnzrwrY7J11moeGhpKQUGB8vXBBx9YfF+a17FG7x9++IHg4GAef/xxdu/ezd69e5k7dy5t27ZV9pHeNzS1uYuLi8XcLigoYNWqVWg0GkaPHq0ca+HChWRlZZGcnMyOHTuo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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a figure and increase the figure size\n",
    "fig = plt.figure(figsize=(12,8))\n",
    "\n",
    "# Create a scatter plot of duration versus year\n",
    "plt.scatter(netflix_movies_col_subset[\"release_year\"], netflix_movies_col_subset[\"duration\"])\n",
    "# Create a title\n",
    "plt.title(\"Movie Duration by Year of Release\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf1880cc",
   "metadata": {
    "dc": {
     "key": "46"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 7. Digging deeper\n",
    "<p>This is already much more informative than the simple plot we created when our friend first gave us some data. We can also see that, while newer movies are overrepresented on the platform, many short movies have been released in the past two decades.</p>\n",
    "<p>Upon further inspection, something else is going on. Some of these films are under an hour long! Let's filter our DataFrame for movies with a <code>duration</code> under 60 minutes and look at the genres. This might give us some insight into what is dragging down the average.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "37a894fc",
   "metadata": {
    "dc": {
     "key": "46"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>country</th>\n",
       "      <th>genre</th>\n",
       "      <th>release_year</th>\n",
       "      <th>duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>#Rucker50</td>\n",
       "      <td>United States</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>2016</td>\n",
       "      <td>56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>55</th>\n",
       "      <td>100 Things to do Before High School</td>\n",
       "      <td>United States</td>\n",
       "      <td>Uncategorized</td>\n",
       "      <td>2014</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>13TH: A Conversation with Oprah Winfrey &amp; Ava ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Uncategorized</td>\n",
       "      <td>2017</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>3 Seconds Divorce</td>\n",
       "      <td>Canada</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>2018</td>\n",
       "      <td>53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>146</th>\n",
       "      <td>A 3 Minute Hug</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>2019</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>162</th>\n",
       "      <td>A Christmas Special: Miraculous: Tales of Lady...</td>\n",
       "      <td>France</td>\n",
       "      <td>Uncategorized</td>\n",
       "      <td>2016</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>171</th>\n",
       "      <td>A Family Reunion Christmas</td>\n",
       "      <td>United States</td>\n",
       "      <td>Uncategorized</td>\n",
       "      <td>2019</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>177</th>\n",
       "      <td>A Go! Go! Cory Carson Christmas</td>\n",
       "      <td>United States</td>\n",
       "      <td>Children</td>\n",
       "      <td>2020</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>178</th>\n",
       "      <td>A Go! Go! Cory Carson Halloween</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Children</td>\n",
       "      <td>2020</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179</th>\n",
       "      <td>A Go! Go! Cory Carson Summer Camp</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Children</td>\n",
       "      <td>2020</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>181</th>\n",
       "      <td>A Grand Night In: The Story of Aardman</td>\n",
       "      <td>United Kingdom</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>2015</td>\n",
       "      <td>59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>200</th>\n",
       "      <td>A Love Song for Latasha</td>\n",
       "      <td>United States</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>2020</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>220</th>\n",
       "      <td>A Russell Peters Christmas</td>\n",
       "      <td>Canada</td>\n",
       "      <td>Stand-Up</td>\n",
       "      <td>2011</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>233</th>\n",
       "      <td>A StoryBots Christmas</td>\n",
       "      <td>United States</td>\n",
       "      <td>Children</td>\n",
       "      <td>2017</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>237</th>\n",
       "      <td>A Tale of Two Kitchens</td>\n",
       "      <td>United States</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>2019</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>242</th>\n",
       "      <td>A Trash Truck Christmas</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Children</td>\n",
       "      <td>2020</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>247</th>\n",
       "      <td>A Very Murray Christmas</td>\n",
       "      <td>United States</td>\n",
       "      <td>Comedies</td>\n",
       "      <td>2015</td>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>285</th>\n",
       "      <td>Abominable Christmas</td>\n",
       "      <td>United States</td>\n",
       "      <td>Children</td>\n",
       "      <td>2012</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>295</th>\n",
       "      <td>Across Grace Alley</td>\n",
       "      <td>United States</td>\n",
       "      <td>Dramas</td>\n",
       "      <td>2013</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>305</th>\n",
       "      <td>Adam Devine: Best Time of Our Lives</td>\n",
       "      <td>United States</td>\n",
       "      <td>Stand-Up</td>\n",
       "      <td>2019</td>\n",
       "      <td>59</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 title         country  \\\n",
       "35                                           #Rucker50   United States   \n",
       "55                 100 Things to do Before High School   United States   \n",
       "67   13TH: A Conversation with Oprah Winfrey & Ava ...             NaN   \n",
       "101                                  3 Seconds Divorce          Canada   \n",
       "146                                     A 3 Minute Hug          Mexico   \n",
       "162  A Christmas Special: Miraculous: Tales of Lady...          France   \n",
       "171                         A Family Reunion Christmas   United States   \n",
       "177                    A Go! Go! Cory Carson Christmas   United States   \n",
       "178                    A Go! Go! Cory Carson Halloween             NaN   \n",
       "179                  A Go! Go! Cory Carson Summer Camp             NaN   \n",
       "181             A Grand Night In: The Story of Aardman  United Kingdom   \n",
       "200                            A Love Song for Latasha   United States   \n",
       "220                         A Russell Peters Christmas          Canada   \n",
       "233                              A StoryBots Christmas   United States   \n",
       "237                             A Tale of Two Kitchens   United States   \n",
       "242                            A Trash Truck Christmas             NaN   \n",
       "247                            A Very Murray Christmas   United States   \n",
       "285                               Abominable Christmas   United States   \n",
       "295                                 Across Grace Alley   United States   \n",
       "305                Adam Devine: Best Time of Our Lives   United States   \n",
       "\n",
       "             genre  release_year  duration  \n",
       "35   Documentaries          2016        56  \n",
       "55   Uncategorized          2014        44  \n",
       "67   Uncategorized          2017        37  \n",
       "101  Documentaries          2018        53  \n",
       "146  Documentaries          2019        28  \n",
       "162  Uncategorized          2016        22  \n",
       "171  Uncategorized          2019        29  \n",
       "177       Children          2020        22  \n",
       "178       Children          2020        22  \n",
       "179       Children          2020        21  \n",
       "181  Documentaries          2015        59  \n",
       "200  Documentaries          2020        20  \n",
       "220       Stand-Up          2011        44  \n",
       "233       Children          2017        26  \n",
       "237  Documentaries          2019        30  \n",
       "242       Children          2020        28  \n",
       "247       Comedies          2015        57  \n",
       "285       Children          2012        44  \n",
       "295         Dramas          2013        24  \n",
       "305       Stand-Up          2019        59  "
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filter for durations shorter than 60 minutes\n",
    "short_movies = netflix_movies_col_subset[netflix_movies_col_subset[\"duration\"] < 60]\n",
    "\n",
    "# Print the first 20 rows of short_movies\n",
    "short_movies[0:20]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba895a44",
   "metadata": {
    "dc": {
     "key": "53"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 8. Marking non-feature films\n",
    "<p>Interesting! It looks as though many of the films that are under 60 minutes fall into genres such as \"Children\", \"Stand-Up\", and \"Documentaries\". This is a logical result, as these types of films are probably often shorter than 90 minute Hollywood blockbuster. </p>\n",
    "<p>We could eliminate these rows from our DataFrame and plot the values again. But another interesting way to explore the effect of these genres on our data would be to plot them, but mark them with a different color.</p>\n",
    "<p>In Python, there are many ways to do this, but one fun way might be to use a loop to generate a list of colors based on the contents of the <code>genre</code> column. Much as we did in Intermediate Python, we can then pass this list to our plotting function in a later step to color all non-typical genres in a different color!</p>\n",
    "<p><em>Note: Although we are using the basic colors of red, blue, green, and black, <code>matplotlib</code> has many named colors you can use when creating plots. For more information, you can refer to the documentation <a href=\"https://matplotlib.org/stable/gallery/color/named_colors.html\">here</a>!</em></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "id": "b516063d",
   "metadata": {
    "dc": {
     "key": "53"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'black',\n",
       " 'blue']"
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define an empty list\n",
    "colors = []\n",
    "\n",
    "# Iterate over rows of netflix_movies_col_subset\n",
    "for lab, row in netflix_movies_col_subset.iterrows() :\n",
    "    if row[\"genre\"] == \"Children\":\n",
    "        colors.append(\"red\")\n",
    "    elif row[\"genre\"] == \"Documentaries\" :\n",
    "        colors.append(\"blue\")\n",
    "    elif row[\"genre\"] == \"Stand-Up\":\n",
    "        colors.append(\"green\")\n",
    "    else:\n",
    "        colors.append(\"black\")\n",
    "        \n",
    "# Inspect the first 10 values in your list        \n",
    "colors[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4520f502",
   "metadata": {
    "dc": {
     "key": "60"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 9. Plotting with color!\n",
    "<p>Lovely looping! We now have a <code>colors</code> list that we can pass to our scatter plot, which should allow us to visually inspect whether these genres might be responsible for the decline in the average duration of movies.</p>\n",
    "<p>This time, we'll also spruce up our plot with some additional axis labels and a new theme with <code>plt.style.use()</code>. The latter isn't taught in Intermediate Python, but can be a fun way to add some visual flair to a basic <code>matplotlib</code> plot. You can find more information on customizing the style of your plot <a href=\"https://matplotlib.org/stable/tutorials/introductory/customizing.html\">here</a>!</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "id": "fcf15241",
   "metadata": {
    "dc": {
     "key": "60"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1AAAAIwCAYAAACImIrfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy86wFpkAAAACXBIWXMAAAsTAAALEwEAmpwYAADRgElEQVR4nOzdeXxU1fk/8M9ksieThJCExRgWCSAIIiig4E4FhIoWrbvFXVxq1brQYl2+UNxq9aeIa7UqWiuuFBSrIgoCKqi4YmwgEAgQEpJM9m1+f8SZ3Js5J3MmObm5d/J5v1591Ty53Dl3mcl95pzzHFdZWZkPREREREREFFJUdzeAiIiIiIjIKZhAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVEBGDRokVIS0vDJ5980i2vP2rUKIwaNapbXruz7Nj2GTNmIC0tDQUFBd3dlB7pyy+/xBlnnIEhQ4YgLS2tW+4PO96XRBQZoru7AUQU+dLS0gAALpcLmzdvxqBBg4TbnX766fjoo48AAA8++CAuueQSi1pI7Rk1ahR27tyJsrKy7m4KOUBFRQV++9vfoqKiAmeffTb69euH1NTU7m4WEZE2TKCIyBLR0dFobGzE888/jzvuuCPo99u3b8eaNWsC21ntiiuuwOzZs5GdnW35azvd22+/3d1NIBvZvHkziouLcfHFF+Pvf/97dzeHiEg7DuEjIkukp6fjqKOOwksvvSRMkF544QX4fD5MmzatG1oH9O7dG0OHDkViYmK3vL6TDRo0SNqrSD1PUVERACArK6ubW0JE1DWYQBGRZS666CLs3bsX77zzjine2NiIpUuXYty4cRg5cqT032/fvh1XX301RowYgczMTOTm5mLOnDn49ttvTdv9/e9/R1paGh555BHhfg4cOICsrCwcfvjh8Pl8ANqfA5Wfn4/rrrsOhx12GLKysnDIIYfg/PPPx1dffRXW8ft8Pjz55JOYOHEi+vTpg0MPPRQ333wzysvLhduHmpeVlpaGGTNmCP/N0qVL8d5772H69Ok4+OCDMWDAgMA2S5cuxYUXXojDDz8cffv2xcEHH4ypU6fi5ZdfNu2roKAAaWlp2LlzZ+D1/P8zvq5srkl9fT3+3//7f5g8eTL69euH7OxsTJkyJZAsi45n1KhRqKqqwu233x4430cccQQeeugh4b8Jxefz4ZFHHsGRRx6JPn36YOTIkfjzn/8Mr9cb2KapqQkjR47EwQcfjMrKSuF+7rzzTqSlpeH5559v9/UuvfRSpKWlYe3atcLfv//++0hLS8MVV1xhipeXl2PhwoU4+uijA+dq2rRpePPNN4P2UV9fjyeffBJnnXVW4BwNGDAAp512Gt59913h644aNQppaWmoq6vDokWLMHbsWGRmZuK2225r93j83n77bcycORM5OTno06cPxo8fj4ULF5rOl/9+mTt3LgDg3nvvDdwvS5cubXf/n3zySeDf5uXl4Xe/+x0OOeQQ9OrVC1u2bAls99Zbb2HWrFkYOHAgsrKyMHbsWNx5552oqKhQOo6O7Ofjjz/G9ddfjwkTJuDggw9G3759MXHiRPz1r39FTU1N0PZerxf3338/jjnmGOTk5OCggw7C6NGjccEFF3Tp5wsRWYcJFBFZ5je/+Q08Hk/QQ+iqVauwZ88e/O53v5P+26+++grHH388Xn75ZYwaNQrXXXcdJk+ejP/85z+YMmUKPvzww8C2Z599NqKiooISAr9ly5ahvr4e55xzDlwuV7ttXrNmDY477ji8/PLLOPzww3HVVVfhpJNOwgcffICpU6figw8+UD7+2267DbfccgsOHDiAiy66CLNnz8YHH3yA008/HQ0NDcr7UfHWW2/h3HPPRVpaGi655BKceuqpgd/ddNNN2LlzJ4455hjMnTsXv/nNb7Bz507MnTsXd999d2C71NRU3HrrrUhJSQEA3HrrrYH/nXfeee2+fkNDA84880z85S9/QW1tLS655BKce+652LVrF6677jpce+21wn/X2NiI2bNn4+2338aUKVNw0UUXoba2FnfeeSfuvffesM/Dbbfdhr/97W849thjcdVVVyE1NRWLFy/G6aefjrq6OgCA2+3GRRddBK/Xi2XLlgmPZenSpUhJScHs2bPbfT3/vL3nnntO+Ptnn30WAHDxxRcHYrt378ZJJ52E+++/H2lpaZgzZw5mz56NgoICzJkzB4sWLTLt48CBA7jttttQWVmJE088Eddccw1OPfVUfPPNNzjnnHMCryFy0UUX4Z///CeOPvpozJ07F7m5ue0eDwAsXLgQF110Eb777jv85je/wVVXXYX4+Hjcf//9mDZtWiAZ9d8v/ntt0qRJgftFtZjDtm3bcPLJJ2P37t04++yzccEFFwR6hW+66Sb87ne/w88//4yZM2fiiiuuQFZWFh566CFTO0IJdz8PP/wwPvzwQ4waNQpz5szBhRdeiNjYWNx33334zW9+Y+pR9/l8OPPMM7Fw4UIkJCTg/PPPx2WXXYaJEyfiq6++wpo1a0z71vn5QkTW4RwoIrJMUlISzjzzTPzzn//Ezp07cfDBBwMAnn/+eSQnJ+M3v/mNsNfI5/PhqquuQnl5OR577DHTw/tHH32EM844A1dccQW2bNmCxMRE9O/fHyeddBLef/99fP311zj88MNN+3v55Zfhcrlw7rnnttve8vJyXHzxxYiJicH777+P4cOHB363detWnHzyybjmmmvw9ddfIy4urt19bdy4EU888QRycnKwevVq9O7dGwBw++23Y9asWdizZ0/gfOjw3//+F6+++iqmTJkS9Lv169cHDbmrr6/HmWeeiYcffhiXXnopDjroIKSlpWHevHl46aWXUFFRgXnz5im//uLFi/Hxxx/jpJNOwr/+9S/ExsYCAObPn49p06Zh6dKlOOWUUzBr1izTvysqKsJhhx2GN954AwkJCQBaErdx48bhsccew0033YSYmBjldnz22Wf45JNPAuf2L3/5Cy688EKsXLkSixcvxo033ggA+N3vfocHHngAzz77LObMmWPax/Lly1FcXIzLL78cSUlJ7b7epEmTMGLECLz99tsoKSkJXGf/sa1atQojRozA0UcfHYjPnTsX+fn5ePrpp3HmmWcG4hUVFZg5cybuu+8+zJw5M5CEpKWl4ZtvvsFBBx1keu3y8nJMmzYNd911F84555zA+TPauXMn1q1bZ2pXez7//HPcf//96N+/Pz744AP069cPQEuP3Ny5c/Gvf/0Ld999dyD5mzdvHpYuXYqVK1di8uTJYd0zALBhwwbcdNNNuP32203xV155Bc888wxmzpyJp556ynRs999/PxYuXIh77rkHCxcubHf/HdnP3/72NwwYMCDoy5YFCxbggQcewFtvvRVIrL///nts3LgRp556Kl566SXT9j6fDwcOHAj8rPPzhYisxR4oIrLU7373OzQ3N+PFF18EAOzatQvvv/8+Zs+ejeTkZOG/2bhxI3788UeMHTs2qOfjhBNOwMyZM7F//36sXLkyEPdv1/Yh5scff8TmzZtxzDHHYODAge229V//+hdKS0tx6623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cCDOO+88vP3228jOzsYnn3wS6K3T+flCRNZiAkVE3eJPf/oTXnzxRSxbtkw6bMtvwoQJGDZsGDZt2oRXXnnF9Ls1a9Zg+fLl6N27t6lUt995552HhoYG/OMf/8CKFSswYMAATJ48WamNF1xwAdLS0nD//ffjs88+C/q9z+fD+vXrUV9fH3Jf/qTtb3/7W2DoDgDU1dXh//7v/4T/5sgjjwQAvPjii6ZJ+iUlJR0uPJGTkwMAQesUffDBB9I1jvw9Rf71oFRceOGFAFqq7hnbXlFRESiVftFFF6k3vIMef/xxU7ubmppwxx13wOfzBfXAAS3J/VlnnYXvv/8ed955J1wuV1jD94wuu+wyNDQ04IILLkBzc3NQ7xPQkkROmjQJK1euxD//+U/hWlc///yz6RhycnJw4MCBoPXPnn/+ee1lry+44AIALT1b/t4moOXev+OOO1BdXY1zzz03rMqIHXHNNdegoaEBV199tamSnZ/X68UXX3yhfT+y98v27dtxxx13BP377du3Y/v27UHxyspKVFVVISYmJjD8T+fnCxFZi0P4iKhbHHTQQcJKYiIulwtLlizB6aefjquuugpvvPEGRo4ciW3btuHtt99GbGwsHn/88cB6MUb+Cf333XcfGhoalNZ+8uvVqxeef/55XHDBBTjllFNw3HHHYfjw4YiJicGuXbvwxRdfoLCwENu3bzdVmhOZOHEirrjiCjz55JM4+uijcdpppyEuLg4rV65Eamoq+vbtG/Rvxo0bh2OPPRaffPIJTjjhBJxwwgk4cOAA3nvvPRx//PFBD9AqLr30UixduhRz5szBrFmz0LdvX/zwww94//33ccYZZ+D1118P+jcnnngiNm/ejAsvvBCnnHIK4uPjcfDBB+Occ86Rvs4111yD999/H++//z6OOeYYTJ06FQ0NDVi+fDl2796Nc845J+xhcR0xfvx4HHvssTjjjDOQkpKC//73v/j+++8xduxY6ZC5Sy+9FM8++yx2796N448/HoccckiHXvu0005DVlYWdu/e3e4aUk8//TRmzZqF66+/Hk888QSOOuoo9OrVC7t378aPP/6ILVu24MUXXwxUE5w7dy4++OADTJ8+HaeffjpSUlLw5ZdfYsOGDZg1axbeeuutDrVXZPz48bjxxhvx4IMP4uijjw683urVq/H1119jxIgRgaqKXen888/H119/jSeffBJjxozBySefjJycHJSXl2PHjh349NNPceKJJwZV3ezsfqZNm4bBgwdj8eLF+P777zF69GgUFhZi1apVOOWUU4J6h7/99ltceOGFGDNmDIYNG4Z+/fqhrKwMq1atwoEDB3DttdcGSuHr/HwhImsxgSIiRxg7diw++ugj3H///fjoo4/wwQcfIDU1FTNmzMBNN92E0aNHC/9dnz59MGXKFKxatUpp7ae2jjvuOKxbtw6PPvooPvjgA3z22WeIjo5Gnz59MH78eNx5553K8z/uvfdeDBkyBE8//TT++c9/Ij09HTNnzsTtt98u7RV78cUXcdddd2HFihV46qmnkJOTE1iI9rXXXgvrWICWKmfLly/HggULsGrVKjQ1NeGwww7DCy+8gNTUVGECddNNN6GiogLvvPMOHn74YTQ2NmLSpEntJlCxsbF4/fXXsWTJEvz73//G008/jaioKBx66KG47bbbAj1UXe2ee+7B22+/jeeffx47duxARkYGrr76asybN086LO+www7DEUccgS+//FLYa6QqJiYGZ599Nh555BGcffbZ0jWk+vXrh9WrV+Opp57CW2+9hddeew0NDQ3IysrCkCFDcO+995rujylTpuBf//oXHnjgAbzxxhuIiorCuHHjsHz5cmzfvl1rAgW0rJ01evRoPPnkk3j11VdRV1eHAQMG4I9//COuv/76oGGQXeW+++7DKaecgmeeeQZr167FgQMHkJqaiv79++Oyyy4LKgOvYz9JSUmBYhBr167F+vXrMXDgQNx888245pprgt4vRxxxBG688UasXbsWq1evxoEDB5Ceno6hQ4fir3/9a9CXBjo/X4jIOq6ysrLg8QJEREQ9VHV1NQ499FDEx8fj22+/7dTwtN/85jf48MMP8emnnyqXQSciInvjHCgiIiKD5557DuXl5bj44os7lTx9/fXX+PDDDzF58mQmT0REEYRD+IiIqMcrLy/HP/7xDxQVFeH5559HRkYGrrrqqg7t65lnnkFRURFeeukluFwu/OlPf9LcWiIi6k4cwkdERD1eQUEBDj/8cMTFxWHUqFG45557AlUQwzVq1Cjs2rULAwcOxB//+EflsvlEROQMTKCIiIiIiIgUcQ4UERERERGRIiZQREREREREiphAERERERERKWIC1QF5eXnd3YQegefZGjzP1uB5tgbPszV4nq3B89z1eI6tEWnnmQkUERERERGRIiZQREREREREiphAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVERERERKSICRQREREREZEiJlBERERERESKmEAREREREREpYgJFRERERESkiAkUERERERGRIiZQREREREREiphAERERERERKWICRUREREREpCi6uxtARERERET2UeBtwILNXhRVN6Ffohvzx3owwBPT3c2yDSZQREREREQEoCV5On1VCbZ5mwKxL4rr8ebU3kyifsEhfEREREREBABYsNlrSp4AYJu3CQs2e7upRfbDBIqIiIiIiAAARdVNwvgeSbwnYgJFREREREQAgH6JbmG8ryTeEzGBIiIiIiIiAMD8sR4M8piTpUGelkIS1IJFJIiIiIiICAAwwBODN6f2xoLNXuypbkJfVuELwgSKiIiIiIgCBnhi8NTx6d3dDNviED4iIiIiIiJFTKCIiIiIiIgUMYEiIiIiIiJSxASKiIiIiIhIERMoIiIiIiIiRUygiIiIiIiIFDGBIiIiIiIiUsQEioiIiIiISFG3JVBPPfUUjjnmGBx88ME4+OCD8atf/QqrVq0K/N7n82HRokUYPnw4+vbtixkzZuCHH34w7aOsrAxXXHEFcnJykJOTgyuuuAJlZWUWHwkREREREfUU3ZZA9e/fH3fddRfWrFmD1atX47jjjsP555+Pb7/9FgDw8MMPY/Hixbj33nvx4YcfIjMzE2eccQa8Xm9gH5dddhm2bNmCZcuWYdmyZdiyZQuuvPLK7jokIiIiIiKKcN2WQM2YMQO/+tWvMHjwYAwZMgS33347kpOT8fnnn8Pn82HJkiX4wx/+gFmzZmHEiBFYsmQJKisrsWzZMgDA1q1b8f777+Ohhx7C+PHjMX78ePz973/HqlWrkJeX112HRUREREREEcwWc6Camprw2muvoaqqCuPHj0dBQQH27t2Lk046KbBNQkICjjnmGGzcuBEA8NlnnyE5ORkTJkwIbDNx4kQkJSUFtiEiIiIiItIpujtf/LvvvsMpp5yC2tpaJCUl4cUXX8TIkSMDCVBmZqZp+8zMTBQVFQEA9u3bh969e8PlcgV+73K5kJGRgX379rX7ujp6qNjLZQ2eZ2vwPFuD59kaPM/W4Hm2Bs9z1+M5toaTznNubm67v+/WBCo3NxeffPIJKioq8NZbb2Hu3Ln4z3/+Y8nrdkZeXl6n90Gh8Txbg+fZGjzP1uB5tgbPszV4nrsez7E1Iu08d+sQvtjYWAwePBhjxozBHXfcgVGjRuGxxx5Dnz59AADFxcWm7YuLi5GVlQUAyMrKQklJCXw+X+D3Pp8P+/fvD2xDRERERESkky3mQPk1Nzejvr4eAwYMQJ8+fbB69erA72pra7F+/frAnKfx48ejsrISn332WWCbzz77DFVVVaZ5UURERERERLp02xC+O++8E6eccgoOOuigQHW9tWvX4t///jdcLhfmzp2LBx98ELm5uRgyZAgeeOABJCUl4cwzzwQADBs2DFOmTMENN9yAhx56CABwww03YOrUqRHVRUhERERERPbRbQnU3r17ccUVV2Dfvn1ISUnByJEjsWzZMpx88skAgOuvvx41NTW4+eabUVZWhnHjxuH111+Hx+MJ7OPpp5/GLbfcgtmzZwMApk+fjvvuu69bjoeIiIiIiCJftyVQS5Ysaff3LpcL8+bNw7x586TbpKWl4cknn9TdNCIiIiIiIiFbzYEiIiIiIiKyMyZQREREREREiphAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVERERERKSICRQREREREZEiJlBERERERESKmEAREREREREpYgJFRERERESkiAkUERERERGRIiZQREREREREiphAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVERERERKSICRQREREREZEiJlBERERERESKmEAREREREREpYgJFRERERESkiAkUERERERGRIiZQREREREREiphAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVERERERKSICRQREREREZEiJlBERERERESKmEAREREREREpYgJFRERERESkiAkUERERERGRIiZQREREREREiphAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVERERERKSICRQREREREZEiJlBERERERESKmEAREREREREpYgJFRERERESkiAkUERERERGRIiZQREREREREiphAERERERERKWICRUREREREpIgJFBERERERkSImUERERERERIqYQBERERERESliAkVERERERKSICRQREREREZGi6O5uABER6VHgbcCCzV4UVTehX6Ib88d6MMAT093NIiIiiihMoIiIIkCBtwGnryrBNm9TIPZFcT3enNqbSRQREZFGHMJHRBQBFmz2mpInANjmbcKCzd5uahEREVFk6rYE6sEHH8SJJ56Igw8+GIcccgjOPvtsfP/996Zt5s6di7S0NNP/pkyZYtqmrq4ON998MwYPHoz+/fvjnHPOwa5du6w8FCKibldU3SSM75HEiYiIqGO6LYFau3YtLr30UqxatQpvv/02oqOjcfrpp+PAgQOm7U444QRs3bo18L9XX33V9Pt58+Zh+fLleOaZZ7By5Up4vV6cffbZaGriQwMR9Rz9Et3CeF9JnIiIiDqm2+ZAvf7666afn3jiCeTk5GDDhg2YPn16IB4XF4c+ffoI91FeXo4XXngBixcvxoknnhjYz6hRo/DRRx/h5JNP7roDICKykfljPfiiuN40jG+Qp6WQBBEREeljmzlQlZWVaG5uRlpamim+fv16DBkyBOPGjcPvf/97FBcXB3731VdfoaGhASeddFIglp2djWHDhmHjxo1WNZ2IqNsN8MTgzam9cdbgBBzbNxZnDU5gAQkiIqIuYJsqfLfddhtGjRqF8ePHB2JTpkzBr3/9awwYMAA7duzAggULcNppp+Gjjz5CXFwc9u3bB7fbjd69e5v2lZmZiX379ll9CERE3WqAJwZPHZ/e3c0gIiKKaLZIoP70pz9hw4YNePfdd+F2t47Xnz17duC/R44ciTFjxmDUqFFYtWoVTjvttA6/Xl5eXqfaq2sfFBrPszV4nq3B82wNnmdr8Dxbg+e56/EcW8NJ5zk3N7fd33d7AjVv3jy8/vrrWL58OQYOHNjutv369UP//v2Rn58PAMjKykJTUxNKSkqQkZER2K64uBhHH320dD+hTkooeXl5nd4HhcbzbA2eZ2vwPFuD59kaPM/W4HnuejzH1oi089ytc6BuvfVWvPbaa3j77bcxdOjQkNuXlJSgqKgoUFRizJgxiImJwerVqwPb7Nq1C1u3bsWECRO6rN1ERERERNQzdVsP1B//+Ee88sorePHFF5GWloa9e/cCAJKSkpCcnIzKykrcc889OO2009CnTx/s2LEDd999NzIzMzFz5kwAQGpqKi688ELccccdyMzMRK9evfDnP/8ZI0eOxAknnNBdh0ZERERERBGq2xKop59+GgAwa9YsU/zWW2/FvHnz4Ha78f333+Nf//oXysvL0adPHxx77LF49tln4fG0luVdtGgR3G43Lr74YtTW1uK4447D448/bppLRUREREREpEO3JVBlZWXt/j4hISForSiRuLg43H///bj//vs1tYyIiIiIiEjMNutAERERERER2R0TKCIiIiIiIkVMoIiIiIiIiBQxgSIiIiIiIlLEBIqIiIiIiEgREygiIiIiIiJFTKCIiIiIiIgUMYEiIiIiIiJSxASKiIiIiIhIUXR3N4CIiKg9Bd4GLNjsRVF1E/olujF/rAcDPDHd3SwiIuqhmEAREZFtFXgbcPqqEmzzNgViXxTX482pvZlEERFRt+AQPiIisq0Fm72m5AkAtnmbsGCzt5taREREPR0TKCIisq2i6iZhfI8kTkRE1NWYQBERkW31S3QL430lcSIioq7GBIqIiGxr/lgPBnnMydIgT0shCSIiou7AIhJERGRbAzwxeHNqbyzY7MWe6ib07eIqfKz4R0REoTCBIiIiWxvgicFTx6d3+euw4h8REangED4iIiKw4h8REalhAkVERARW/CMiIjUcwkdERAS9Ff84l4qIKHIxgSIiIkJLxb8viutNw/g6UvGPc6mIiCIbh/ARERGhteLfWYMTcGzfWJw1OKFDSQ/nUhERRTb2QBGRLXDIE9mBjop/nEtFRBTZmEARUbfjkCeKJDrnUhERkf1wCB8RdTsOeaJIMn+sB4M85mSpI3OpiIjIntgDRUTdjkOeKJL451It2OzFnuom9OWQVCKiiMIEioi6HYc8UaTRMZeKiIjsiUP4iKjbccgTEREROQV7oIio23HIExFReFi5lKj7MIEiIlvgkCciIjWsXErUvTiEj4iIiMhBWLmUqHsxgSIiIiJyEFYuJepeTKCIiIiIHISVS4m6FxMoIiIiIgdh5VKi7sUiEkREREQOwsqlRN2LCRQRERGRw7ByKVH34RA+IiIiIiIiRUygiIiIiIiIFDGBIiIiIiIiUsQEioiIiIiISBETKCIiIiIiIkVMoIiIiIiIiBSxjDkREREROUKBtwELNntRVN2Eflz/iroJEygiIiIisr0CbwNOX1WCbd6mQOyL4nq8ObU3kyiyFIfwEREREZHtLdjsNSVPALDN24QFm73d1CLqqZhAEREREZHtFVU3CeN7JHGirsIEioiIiIhsr1+iWxjvK4kTdRUmUERERERke/PHejDIY06WBnlaCkkQWYlFJIiIiIjI9gZ4YvDm1N5YsNmLPdVN6MsqfNRNmEAREREROUxPLec9wBODp45P7+5mEHruPQgwgSIiIiJyFJbzpu7W0+9BzoEiIiIichC7lfMu8Dbg8jWlmPlOMS5fU4oCb0O3tIOsY7d70GrsgSIiIiJyEDuV8+7pPRE9lZ3uwe7AHigiIiIiB7FTOe+e3hPRU9npHuwOTKCIiIiIHMRO5bx7ek9ET2Wne7A7cAgfERERkYPYqZx3T++JsJKdqt7Z6R7sDkygiIiIqEez04OpKruU854/1oMviutNw/h6Uk+EVew418wu92B3YAJFREREPZYdH0ydpKf3RFilvblmPTWJ6U5MoIiIiKjH4oNp59mtJ8KJPYqhcK6ZvTCBIiIioh6LD6aRJVJ7FDnXzF5YhY+IiIh6LD6YRpZILave06ve2U23JVAPPvggTjzxRBx88ME45JBDcPbZZ+P77783bePz+bBo0SIMHz4cffv2xYwZM/DDDz+YtikrK8MVV1yBnJwc5OTk4IorrkBZWZmFR0JERERO1ZMfTAu8Dbh8TSlmvlOMy9eUosDb0N1N6rRI7VH0zzU7a3ACju0bi7MGJzi+V83Jum0I39q1a3HppZdi7Nix8Pl8+Otf/4rTTz8dGzduRK9evQAADz/8MBYvXozFixcjNzcX9913H8444wx8/vnn8HhaPtguu+wyFBYWYtmyZQCA3//+97jyyivxyiuvdNehEVEXicRx7UTUvXpqEQQOdXMeu80168m6LYF6/fXXTT8/8cQTyMnJwYYNGzB9+nT4fD4sWbIEf/jDHzBr1iwAwJIlS5Cbm4tly5bh4osvxtatW/H+++/j3Xffxfjx4wEAf//73zF9+nTk5eUhNzfX8uMioq4RqX/siaj79cQH00gtnsGy6mQF28yBqqysRHNzM9LS0gAABQUF2Lt3L0466aTANgkJCTjmmGOwceNGAMBnn32G5ORkTJgwIbDNxIkTkZSUFNiGiCJDpI5rJyLqDhzqRtRxtqnCd9ttt2HUqFGBnqS9e/cCADIzM03bZWZmoqioCACwb98+9O7dGy6XK/B7l8uFjIwM7Nu3T/paeXl5nW6vjn1QaDzP1nDCec7fHwcgeAhGfkkl8vJKrG9QBzjhPEcCnmdr8Dxbo6vOc3JTDIDgpCKpqQp5eWVd8ppWuqV/63/X7ylB3h75tryXreGk8xxqFFvYCdTevXtRUlICl8uF3r17Iysrq8ON8/vTn/6EDRs24N1334Xb3fVjVDs7tI/DA63B82wNp5znwbtLsamiJjjeOxm5uTnd0KLwOOU8Ox3PszV4nq3Rlef53r4N2NpmWPQgjxv3Hp/Vo3preC9bI9LOc8gEqrKyEm+88Qb+85//4PPPPw+qcJeWloajjjoKM2bMwBlnnBEo7qBq3rx5eP3117F8+XIMHDgwEO/Tpw8AoLi4GAcffHAgXlxcHEjasrKyUFJSAp/PF+iF8vl82L9/v5bEjojsg+PaiYj06anFM4h0kCZQpaWlePDBB/Hcc8+htrYWI0eOxK9//WsMHDgQaWlp8Pl8KCsrQ0FBAb766ivceOONmDdvHubMmYMbb7wRvXv3Dvnit956K9544w0sX74cQ4cONf1uwIAB6NOnD1avXo2xY8cCAGpra7F+/XrcfffdAIDx48ejsrISn332WWAe1GeffYaqqirTvCgicj7+sSci0svK4hmsokqRRJpAjR49GgMHDsRdd92FWbNmISMjo90d7d+/H2+99Raee+45PP/889i5c2e72//xj3/EK6+8ghdffBFpaWmBOU9JSUlITk6Gy+XC3Llz8eCDDyI3NxdDhgzBAw88gKSkJJx55pkAgGHDhmHKlCm44YYb8NBDDwEAbrjhBkydOjWiugmJqEVPrJRF+vABzll4vSIHq6hSpJEmUP/4xz9wyimnKO8oIyMDl156KS699FK89957Ibd/+umnASBQotzv1ltvxbx58wAA119/PWpqanDzzTejrKwM48aNw+uvv24aJvj000/jlltuwezZswEA06dPx3333afcbiIiinx8gHMWXq/IEqkl06nnkiZQ4SRPHfm3bedSibhcLsybNy+QUImkpaXhySefDKd5RGQxfpNM3Y0PcM7C6xVZIrVkOvVctiljTkSRid8kkx3wAc5ZVK8Xv5xxhn6J4grLfSVxIrsLK4HaunUrli5diu3bt6OsrAw+n8/0e5fLhbfffltrA4nI2fhNMtkBH+BCs1MyonK9+OWMc8wf68H6PbUorG59bsxOdLGK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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set the figure style and initalize a new figure\n",
    "plt.style.use('fivethirtyeight')\n",
    "fig = plt.figure(figsize=(12,8))\n",
    "\n",
    "# Create a scatter plot of duration versus release_year\n",
    "plt.scatter(netflix_movies_col_subset[\"release_year\"], netflix_movies_col_subset[\"duration\"])\n",
    "\n",
    "# Create a title and axis labels\n",
    "plt.title(\"Movie duration by year of release\")\n",
    "plt.xlabel(\"Release year\")\n",
    "plt.ylabel(\"Duration (min)\")\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3a59fbf",
   "metadata": {
    "dc": {
     "key": "67"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 10. What next?\n",
    "<p>Well, as we suspected, non-typical genres such as children's movies and documentaries are all clustered around the bottom half of the plot. But we can't know for certain until we perform additional analyses. </p>\n",
    "<p>Congratulations, you've performed an exploratory analysis of some entertainment data, and there are lots of fun ways to develop your skills as a Pythonic data scientist. These include learning how to analyze data further with statistics, creating more advanced visualizations, and perhaps most importantly, learning more advanced ways of working with data in <code>pandas</code>. This latter skill is covered in our fantastic course <a href=\"www.datacamp.com/courses/data-manipulation-with-pandas\">Data Manipulation with pandas</a>.</p>\n",
    "<p>We hope you enjoyed this application of the skills learned in Intermediate Python, and wish you all the best on the rest of your journey!</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "e2d2ff5e",
   "metadata": {
    "dc": {
     "key": "67"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Are we certain that movies are getting shorter?\n",
    "are_movies_getting_shorter = \"Exactly\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}