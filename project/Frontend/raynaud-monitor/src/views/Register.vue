<template>
    <AccessGenericPage
        :title="'Register'"
        :icon="'mdi-register'"
        :action="register"
        :actionName="'Create account'"
        :loading="loading"
        :valid="valid"
    >
        <v-form v-model="valid">
            <v-text-field
                v-model="form.email"
                :rules="[rules.required, rules.email]" required counter="50"
                :disabled="loading"
                prepend-inner-icon="mdi-email"
                label="Email"
                type="email"
                autofocus
            />
            <v-text-field
                v-model="form.password"
                :rules="[rules.required, rules.min]" required counter="50"
                :disabled="loading"
                prepend-inner-icon="mdi-lock"
                label="Password"
                type="password"
            />
            <v-text-field
                v-model="form.password2"
                :rules="[rules.required, rules.min, rules.match]" required counter="50"
                v-on:keyup.13="register()"
                :disabled="loading"
                prepend-inner-icon="mdi-lock"
                label="Repeat password"
                type="password"
            />
        </v-form>

        <template v-slot:info>
            <router-link :to="'/login'">Have an account?</router-link>
        </template>
    </AccessGenericPage>
</template>

<script>
import Access from '@/global/fetch/Access'
import AccessGenericPage from '@/components/AccessGenericPage.vue';

// Vuex
import { mapMutations } from 'vuex'

export default {
    data() {
        return {
            loading: false,
            valid: false,
            form: {
                email: "",
                password: "",
                password2: ""
            },
            rules: {
                required: value => !!value || "Requerido.",
                email: value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) || "Email inválido.",
                min: v => v.length >= 8 || "Mínimo 8 caracteres.",
                match: v => v === this.form.password || "Las contraseñas no coinciden.",
            },
        };
    },
    methods: {
        ...mapMutations(['setGenericSnackbar']),
        async register() {
            const { form } = this;
            if (form.password != form.password2) {
                
                //TODO snackbar
                return
            }
            if (form.email && form.password) {
                this.loading = true;
                const response = await Access.register(form.email, form.password);
                this.loading = false;
                if (response === 0) {
                    console.log("Register success");
                    this.$router.push("/"); //IDEA welcome?
                    await Access.login(form.email, form.password);
                }else {
                    console.log("Register error");
                    //TODO snackbar
                }
            }
        },
    },
    components: { AccessGenericPage }
};
</script>