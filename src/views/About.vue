<template>
	<div class="page-about container px-10 mx-auto text-gray-400">
		<h1>
			Mauritius
			<span class="font-light">Sea Cables</span>
		</h1>
		<router-link class="button" :to="{name: 'home'}">View Map</router-link>
		<h2>Aim</h2>
		<p>The aim of this project is to profile a simple interface to reflect the current status of internet connectitivity of Mauritius.</p>
		<h2>How it works?</h2>
		<p>The data comes from independantly hosted tests that rely on the Speedtest-cli utility.</p>
		<p>
			There is a companion project which performs the tests and then pushes it to the gihtub repo of the tester.
			<a
				href="https://github.com/reallyaditya"
			>View Companion Project</a>
		</p>

		<p class="font-bold pt-3">Here is the list of sources currrently available:</p>
		<ul v-if="sources">
			<li v-for="item in sources">
				{{item.name}}
				<a :href="item.url" class="button" target="_blank">View</a>
			</li>
		</ul>
		<h2 id="source">Would you like to be a source?</h2>
		<p>// TODO insert instructions on how to become a source</p>
		<ul>
			<li>Clone repo</li>
			<li>Run it with cron</li>
			<li>
				Send a PR to add your repo as source to
				<a
					href="https://github.com/MrSunshyne/mauritius-sea-cable/blob/master/public/sources.json"
				>this file</a>
			</li>
		</ul>
		<br />
		<p>The file is expected to be in the following format</p>
		<pre class="border border-black my-2 font-mono text-xs">			
		// file: all-servers.json
		{
			LION : SpeedtestResult,
			MARS:  SpeedtestResult,
			SAFE1: SpeedtestResult,
			SAFE2: SpeedtestResult,
			SAFE3: SpeedtestResult
		}
		// Where Speedtest result has the following signature
		Interface SpeedtestResult {
			timestamp: '',
			upload: '',
			download: '',
			ping: ''
		}
		</pre>
		<a
			href="https://mrsunshyne.github.io/mauritius-sea-cable/all-servers.json"
		>View example source file</a>
		<h2>Is this Official?</h2>
		<p>
			Absolutely not. This is a community effort. All the code are open source and available online should you wish to verify the
			<a
				href="https://github.com/MrSunshyne/mauritius-sea-cable"
			>front-end client</a> or the
			<a href="https://github.com/reallyaditya">backend-end service</a>
		</p>

		<h2 id="contribute">Contribute</h2>
		<p>This project is opensource on github. If you think something can be improved or a new feature would be useful. Feel free to contribute by sending a PR.</p>
		<h2>Tech Stack</h2>
		<ul>
			<li>VueJS</li>
			<li>TailwindCSS</li>
			<li>Python</li>
			<li>Speedtest-cli</li>
			<li>Git</li>
		</ul>
		<h2>Credits</h2>
		<p>
			The project is inspired by
			<a href="https://baliseacable.com">Bali Sea Cable</a> built by
			<a href="https://twitter.com/levelsio">@levelsio</a>
		</p>
		<p>
			The companion side project which provides the data sources was written in python by
			<a
				href="https://github.com/reallyaditya"
			>Adiyta</a>
		</p>
	</div>
</template>

<style scoped>
.page-about {
	padding-top: 100px;
	padding-bottom: 100px;
	max-width: 700px;
}
h1 {
	@apply text-5xl font-black pb-5 text-white;
}

h2 {
	@apply text-2xl font-bold pt-3 pb-2 mt-5;
	color: #2bde73;
	border-top: 1px solid rgba(255, 255, 255, 0.1);
}

a {
	@apply underline text-white;
}

p {
	@apply pb-1;
	/* line-height: 2em; */
}

.button {
	text-decoration: none;
}

ul {
	padding-top: 5px;
	list-style-type: disc;
	list-style-position: inside;
}
</style>

<script>
export default {
	data() {
		return {
			publicPath:
				process.env.NODE_ENV === "production" ? "/mauritius-sea-cable/" : "/",
			sources: null
		};
	},
	methods: {
		loadSources() {
			fetch(`${this.publicPath}sources.json`)
				.then(json => json.json())
				.then(response => {
					this.sources = response;
				})
				.catch(error => {
					this.error = error;
				});
		}
	},
	mounted() {
		this.loadSources();
	}
};
</script>