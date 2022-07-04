<template>
    <AccessGenericPage
        :title="'Login'"
        :icon="'mdi-login'"
        :action="login"
        :actionName="'Login'"
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
                v-on:keyup.13="login()"
                :disabled="loading"
                prepend-inner-icon="mdi-lock"
                label="Password"
                type="password"
            />
        </v-form>

        <template v-slot:info>
            <router-link :to="'/register'">Create an account</router-link>
        </template>

    </AccessGenericPage>
    
</template>

<script>
import Access from '@/global/fetch/Access'
import AccessGenericPage from '@/components/AccessGenericPage.vue'

// Vuex
import { mapMutations } from 'vuex'

export default {
    data() {
        return {
            loading: false,
            valid: false,
            form: {
                email: "",
                password: ""
            },
            rules: {
                required: value => !!value || "Requerido.",
                email: value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) || "Email inválido.",
                min: v => v.length >= 8 || "Mínimo 8 caracteres.",
            },
        };
    },
    methods: {
        ...mapMutations(['setGenericSnackbar']),
        async login() {
            try {

                const { form } = this;
                if (form.email && form.password) {
                    this.loading = true;
                    const login = await Access.login(form.email, form.password);
                    this.loading = false;
                    if (login === 0) {
                        await Access.me();
                        this.$router.push("/");
                    } else {
                        this.setGenericSnackbar({
                            show: true,
                            type: 'error',
                            message: 'Email o contraseña incorrectos.'
                        })
                    }
                }
                
            } catch (error) {
                console.log(error);
            }
        },
    },
    components: { AccessGenericPage }
}
</script>